

import asyncio
import os
from playwright.async_api import async_playwright

HOME_URL = "https://fantasiasonline.com"
CHATS_URL = "https://fantasiasonline.com/u/chats"
STORAGE_STATE = "session_state.json"


async def realizar_autenticacao():
    print("=" * 60)
    print("MÓDULO DE AUTENTICAÇÃO E GERENCIAMENTO DE SESSÃO")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        # Se já existir sessão, tenta reutilizar para verificar se ainda é válida
        if os.path.exists(STORAGE_STATE):
            print("→ Sessão salva encontrada. Testando validade no site...")
            context = await browser.new_context(storage_state=STORAGE_STATE)
        else:
            print("→ Nenhuma sessão salva encontrada. Abrindo navegador limpo...")
            context = await browser.new_context()

        page = await context.new_page()
        await page.goto(CHATS_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        # Se for redirecionado para a home ou com callbackUrl, precisa logar
        if "callbackUrl" in page.url or page.url.strip("/") == HOME_URL.strip("/"):
            print("\n" + "!" * 60)
            print("AÇÃO NECESSÁRIA:")
            print("1. Na janela do navegador aberta, faça o login na sua conta.")
            print("2. Resolva qualquer captcha/verificação de robô que aparecer.")
            print("3. Quando estiver na tela de chats, volte ao PyCharm.")
            print("!" * 60 + "\n")

            input("--> Pressione [ENTER] no terminal do PyCharm assim que o login estiver concluído... <--\n")

            # Salva os novos cookies de sessão validados
            await context.storage_state(path=STORAGE_STATE)
            print("✓ Nova sessão capturada e salva em session_state.json com sucesso!")
        else:
            print("✓ Sessão existente validada com sucesso! Você já está conectado.")

        await browser.close()
        print("✓ Processo de login encerrado.")


if __name__ == "__main__":
    asyncio.run(realizar_autenticacao())