import asyncio
import os
import urllib.request
from playwright.async_api import async_playwright

# Configurações do Alvo
TARGET_URL = "https://fantasiasonline.com/u/chats"
DOWNLOAD_DIR = "./downloads_perfil"


async def extrair_e_baixar_imagem():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    async with async_playwright() as p:
        # Abre o navegador visível (headless=False permite você logar se necessário)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print(f"Acessando: {TARGET_URL}")
        await page.goto(TARGET_URL, wait_until="networkidle")

        # Se precisar logar manualmente na 1ª vez, desmante a linha abaixo:
        # input("Faça o login no navegador e pressione Enter aqui no terminal...")

        # Seletor CSS generico para pegar a imagem da foto do perfil/chat
        seletor_imagem = "div.avatar img, div img[src*='upload'], div.chat-user img"

        try:
            await page.wait_for_selector(seletor_imagem, timeout=10000)

            # Captura a URL contida no atributo 'src' ou 'currentSrc'
            img_element = page.locator(seletor_imagem).first
            img_url = await img_element.get_attribute("src") or await img_element.evaluate("el => el.currentSrc")

            if img_url:
                print(f"URL da Imagem encontrada: {img_url}")

                # Garante URL completa se for caminho relativo
                if img_url.startswith("//"):
                    img_url = "https:" + img_url
                elif img_url.startswith("/"):
                    img_url = "https://fantasiasonline.com" + img_url

                # Nome do arquivo local
                filename = os.path.basename(img_url.split("?")[0]) or "perfil_avatar.jpg"
                filepath = os.path.join(DOWNLOAD_DIR, filename)

                # Download do arquivo de imagem
                urllib.request.urlretrieve(img_url, filepath)
                print(f"✓ Imagem salva em: {os.path.abspath(filepath)}")

                # Abre busca reversa no Yandex (ótimo para identificar bots/fotos vazadas)
                await buscar_reversa(context, img_url)

                # Mantém o navegador aberto por uns segundos para você analisar
                await page.wait_for_timeout(10000)
            else:
                print("Não foi possível capturar o atributo da imagem.")

        except Exception as e:
            print(f"Erro ao localizar/baixar o elemento: {e}")

        await browser.close()


async def buscar_reversa(context, img_url):
    print("Abrindo aba de busca reversa de imagem...")
    yandex_search = f"https://yandex.com/images/search?rpt=imageview&url={img_url}"
    new_tab = await context.new_page()
    await new_tab.goto(yandex_search)


if __name__ == "__main__":
    asyncio.run(extrair_e_baixar_imagem())