import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True   # <- segurança ativada

EMAIL = "dudu475894@gmail.com"
SENHA = "Dudu475894@"
URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


def abrir_sistema():
    pyautogui.press("win")
    pyautogui.write("opera")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write(URL)
    pyautogui.press("enter")
    time.sleep(10)


def fazer_login():
    pyautogui.click(x=699, y=392)
    pyautogui.write(EMAIL)
    pyautogui.press("tab")
    pyautogui.write(SENHA)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(5)


def cadastrar_produtos(tabela):
    for _, produto in tabela.iterrows():
        pyautogui.click(x=689, y=278)

        pyautogui.write(str(produto["codigo"]))
        pyautogui.press("tab")

        pyautogui.write(str(produto["marca"]))
        pyautogui.press("tab")

        pyautogui.write(str(produto["tipo"]))
        pyautogui.press("tab")

        pyautogui.write(str(produto["categoria"]))
        pyautogui.press("tab")

        pyautogui.write(str(produto["preco_unitario"]))
        pyautogui.press("tab")

        pyautogui.write(str(produto["custo"]))
        pyautogui.press("tab")

        if not pd.isna(produto["obs"]):
            pyautogui.write(str(produto["obs"]))

        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(1)  # <- pequena pausa


def main():
    abrir_sistema()
    fazer_login()
    tabela = pd.read_csv("produtos.csv")
    cadastrar_produtos(tabela)
    print("✅ Automação finalizada com sucesso!")


if __name__ == "__main__":
    main()