import asyncio
import os
import urllib.parse
from playwright.async_api import async_playwright

CHATS_URL = "https://fantasiasonline.com/u/chats"
STORAGE_STATE = "session_state.json"
DOWNLOAD_DIR = "./downloads_perfil"

MAX_FOTOS_CARROSSEL = 3
MAX_FOTOS_CHAT = 5


def extrair_url_real_imagem(raw_url):
    """
    Decodifica URLs otimizadas do Next.js (_next/image?url=...)
    e retorna o link direto limpo e decodificado do S3 Amazon.
    """
    if not raw_url:
        return ""

    # Se contém parâmetro url=, faz a decodificação do Next.js
    if "url=" in raw_url:
        parsed = urllib.parse.urlparse(raw_url)
        params = urllib.parse.parse_qs(parsed.query)
        if "url" in params and params["url"]:
            return urllib.parse.unquote(params["url"][0])

    return urllib.parse.unquote(raw_url)


def normalizar_url(url):
    """
    Garante que a URL seja absoluta com o protocolo https.
    """
    if not url:
        return ""
    if url.startswith("//"):
        return "https:" + url
    elif url.startswith("/"):
        return "https://fantasiasonline.com" + url
    return url


async def extrair_e_verificar_perfil_e_chat():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    if not os.path.exists(STORAGE_STATE):
        print("⚠️ Nenhuma sessão salva encontrada! Execute o 'login.py' primeiro.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state=STORAGE_STATE)
        page_principal = await context.new_page()

        print(f"→ Carregando página de chats: {CHATS_URL}")
        await page_principal.goto(CHATS_URL, wait_until="domcontentloaded")
        await page_principal.wait_for_timeout(4000)

        seletor_foto_perfil = "img.aspect-3\\/4, img[alt='avatar']"

        seletores_botao_next = [
            "button[aria-label*='Next']",
            "button[aria-label*='próximo']",
            "button[aria-label*='Proximo']",
            "button.embla__next",
            "button:has(svg.lucide-chevron-right)",
            "button:has(svg.lucide-arrow-right)",
            "div[class*='carousel'] button:last-child"
        ]

        # Seletor focado exatamente na tag enviada por você
        seletor_imagens_chat = "img[alt='imagem'], img.rounded-md"

        urls_processadas = set()
        abas_busca_abertas = []

        # ==========================================
        # ETAPA 1: VARRER FOTOS DO PERFIL / CARROSSEL
        # ==========================================
        print("\n=== [1/2] VARRENDO FOTOS DE PERFIL (CARROSSEL) ===")

        for i in range(MAX_FOTOS_CARROSSEL):
            try:
                foto_el = page_principal.locator(seletor_foto_perfil).first
                if await foto_el.is_visible(timeout=2000):
                    src_raw = await foto_el.get_attribute("src") or await foto_el.evaluate("el => el.currentSrc")

                    if src_raw:
                        # 1. Normaliza
                        src_norm = normalizar_url(src_raw)
                        # 2. Decodifica parâmetro url=
                        url_limpa = extrair_url_real_imagem(src_norm)

                        if url_limpa and url_limpa not in urls_processadas:
                            urls_processadas.add(url_limpa)
                            print(f"[Perfil {len(urls_processadas)}] URL: {url_limpa}")

                            filename = f"perfil_{len(urls_processadas)}_" + (
                                        os.path.basename(url_limpa.split("?")[0]) or "avatar.png")
                            filepath = os.path.join(DOWNLOAD_DIR, filename)

                            response = await context.request.get(url_limpa)
                            if response.status == 200:
                                with open(filepath, "wb") as f:
                                    f.write(await response.body())
                                print(f"   ✓ Foto salva em: {filepath}")

                                yandex_url = f"https://yandex.com/images/search?rpt=imageview&url={urllib.parse.quote(url_limpa)}"
                                aba_busca = await context.new_page()
                                await aba_busca.goto(yandex_url)
                                abas_busca_abertas.append(aba_busca)
                                print("   ✓ Aba de busca aberta no Yandex.")

                if i < MAX_FOTOS_CARROSSEL - 1:
                    avancou = False
                    for seletor_btn in seletores_botao_next:
                        btn = page_principal.locator(seletor_btn).first
                        if await btn.is_visible():
                            await btn.click()
                            await page_principal.wait_for_timeout(1200)
                            avancou = True
                            print("   → Avançou carrossel do perfil...")
                            break
                    if not avancou:
                        break
            except Exception as e:
                print(f"   ⚠️ Erro na extração do carrossel: {e}")
                break

        # ==========================================
        # ETAPA 2: VARRER MENSAGENS E FOTOS DO CHAT
        # ==========================================
        print("\n=== [2/2] VARRENDO HISTÓRICO DE MENSAGENS DO CHAT ===")

        try:
            chat_container = page_principal.locator("main, div.overflow-y-auto, div[class*='chat']").first
            if await chat_container.is_visible():
                print("→ Scrollando histórico do chat para carregar mídias enviadas...")
                for _ in range(3):
                    await chat_container.evaluate("el => el.scrollTop = el.scrollTop - 600")
                    await page_principal.wait_for_timeout(800)

            imgs_chat = page_principal.locator(seletor_imagens_chat)
            qtd_imgs_chat = await imgs_chat.count()
            print(f"✓ Mídias de chat encontradas: {qtd_imgs_chat}")

            fotos_chat_baixadas = 0
            for k in range(qtd_imgs_chat):
                if fotos_chat_baixadas >= MAX_FOTOS_CHAT:
                    break

                img_el = imgs_chat.nth(k)
                src_chat = await img_el.get_attribute("src") or await img_el.evaluate("el => el.currentSrc")

                if src_chat:
                    # 1. Normaliza a URL
                    src_norm = normalizar_url(src_chat)
                    # 2. Decodifica para obter a URL limpa do S3 Amazon
                    url_chat_limpa = extrair_url_real_imagem(src_norm)

                    # 3. Valida se é uma imagem válida de perfil/chat no S3
                    is_valid_s3 = any(termo in url_chat_limpa.lower() for termo in
                                      ["fictitious-profiles", "s3", "amazonaws.com", "photos"])

                    if is_valid_s3 and url_chat_limpa not in urls_processadas:
                        urls_processadas.add(url_chat_limpa)
                        fotos_chat_baixadas += 1

                        print(f"[Chat Foto {fotos_chat_baixadas}] URL: {url_chat_limpa}")

                        filename = f"chat_{fotos_chat_baixadas}_" + (
                                    os.path.basename(url_chat_limpa.split("?")[0]) or "chat_img.png")
                        filepath = os.path.join(DOWNLOAD_DIR, filename)

                        try:
                            response = await context.request.get(url_chat_limpa)
                            if response.status == 200:
                                with open(filepath, "wb") as f:
                                    f.write(await response.body())
                                print(f"   ✓ Foto do chat salva em: {filepath}")

                                yandex_url = f"https://yandex.com/images/search?rpt=imageview&url={urllib.parse.quote(url_chat_limpa)}"
                                aba_busca = await context.new_page()
                                await aba_busca.goto(yandex_url)
                                abas_busca_abertas.append(aba_busca)
                                print("   ✓ Aba de busca Yandex aberta para imagem do chat.")
                            else:
                                print(f"   ⚠️ Status {response.status} ao baixar imagem.")
                        except Exception as download_err:
                            print(f"   ⚠️ Erro no download da mídia: {download_err}")

        except Exception as e:
            print(f"   ⚠️ Erro ao varrer mensagens do chat: {e}")

        # ==========================================
        # PAUSA E LIMPEZA DE RECURSOS (RAM)
        # ==========================================
        if abas_busca_abertas:
            print("\n" + "=" * 65)
            print(f"→ Processamento do perfil concluído com {len(abas_busca_abertas)} foto(s) no Yandex.")
            print(
                "→ Verifique as abas no navegador e pressione [ENTER] no PyCharm para fechar as abas e ir ao próximo...")
            print("=" * 65)
            input()

            for aba in abas_busca_abertas:
                await aba.close()
            print("✓ Abas do Yandex fechadas e RAM liberada!")
        else:
            print("\n⚠️ Nenhum resultado extraído para este perfil.")

        print("\nPressione [ENTER] no terminal para encerrar...")
        input()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(extrair_e_verificar_perfil_e_chat())