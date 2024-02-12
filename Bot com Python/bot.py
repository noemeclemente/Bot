import pyautogui

pyautogui.PAUSE = 2

# abrir a ferramenta no computador
pyautogui.press("win")
pyautogui.write("Login.xlsx")
pyautogui.press("backspace")
pyautogui.press('enter')
# preecnher o login
pyautogui.click(x=511, y=254)
pyautogui.write('Noeme')
# preencher a senha
pyautogui.click(x=471, y=294)
pyautogui.write('senha')
# clicar em fazer login
pyautogui.click(x=340, y=426)
pyautogui.click(x=340, y=426)
