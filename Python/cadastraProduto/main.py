from tkinter.constants import SEL_LAST

import pyautogui as pag
import time
import pandas as pd
from mouseinfo import MouseInfoWindow

pag.PAUSE= 1

#abrir o navegador
pag.press("win")
pag.write("firefox")
pag.press("enter")

#entrar no site
pag.click(x=1300, y=70)
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")
time.sleep(3)

# Fazer Login
pag.click(x=1295, y=402)# caixa de email
time.sleep(0.3)
pag.click(x=1295, y=402)# caixa de email
time.sleep(0.3)
pag.write("Teste@gmail.com")
pag.press("tab")
pag.write("Teste@gmail.com")
pag.press("tab")
pag.write("suasenhao")
pag.press("enter")
#time.sleep(3)

#importar base de produtos
tabela = pd.read_csv("produtos.csv")

#cadastrar produtos

for linha in tabela.index:
    # clicar no campo de código
    pag.click(x=1211, y=296)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pag.write(str(codigo))
    # passar para o proximo campo
    pag.press("tab")
    # preencher o campo
    pag.write(str(tabela.loc[linha, "marca"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "tipo"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "categoria"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "preco_unitario"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "custo"]))
    pag.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pag.write(str(tabela.loc[linha, "obs"]))
    pag.press("tab")
    pag.press("enter") # cadastra o produto (botao enviar)
    pag.scroll(5000)