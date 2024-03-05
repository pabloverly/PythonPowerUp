import pandas
import pyautogui
import time

pyautogui.PAUSE = 0.3

# pyautogui.hotkey("win", "r") //duas teclas
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(732, 352)
pyautogui.write("pablo")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")


time.sleep(5)


tabela = pandas.read_csv("produtos.csv")
print(tabela)


print(pyautogui.position())  # capturar posicao
pyautogui.click(762, 237)


for linha in tabela.index:
    # Produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Obs
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
        pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(2000)
    pyautogui.click(762, 237)

# time.sleep(1)
