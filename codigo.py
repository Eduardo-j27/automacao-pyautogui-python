# Passos a passo do meu programa
# Passo 1: Entrar no sistema da empresa
#abrir navegador
import pyautogui 
import time
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press ("win")
pyautogui.write ("opera")
pyautogui.press ("enter")

pyautogui.write (link)
pyautogui.press ("enter")
#pausa pro site carregar
time.sleep(15)

# Passo 2: Fazer login
pyautogui.click (x=699, y=392)
pyautogui.write ("dudu475894@gmail.com")
pyautogui.press ("tab")
pyautogui.write ("Dudu475894@")
pyautogui.press ("tab")
pyautogui.press ("enter")

# Passo 3: Abrir a base de dados 
import pandas as pd 

#importar base de produto
tabela = pd.read_csv("produtos.csv")
print (tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=689, y=278) # Aqui parece haver espaços extras
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
#fim da linha de codigos