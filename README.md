# Automação de Login com PyAutoGUI

Este projeto é um conjunto de scripts Python que utiliza a biblioteca `pyautogui` para automatizar o processo de login em uma ferramenta específica no computador. 

## Requisitos

- **Python 3.x**: O script foi desenvolvido para Python 3.
- **PyAutoGUI**: Biblioteca para automação de GUI.
  - Pode ser instalada via pip:
    ```bash
    pip install pyautogui
    ```

## Funcionalidades

1. **Abrir o Arquivo**: O script usa `pyautogui` para abrir o arquivo `Login.xlsx` no computador.
2. **Preencher Login**: Insere o nome de usuário em um campo específico da interface.
3. **Preencher Senha**: Insere a senha em outro campo da interface.
4. **Realizar Login**: Clica no botão de login para acessar a ferramenta.
5. **Posição do Cursor**: Um segundo script imprime a posição do cursor para ajudar a ajustar as coordenadas de clique.

## Código

### Script de Automação de Login

O script realiza as seguintes ações:

1. **Abrir a Ferramenta**:
   - Pressiona a tecla "Win" para abrir o menu iniciar.
   - Digita "Login.xlsx" e pressiona "Enter" para abrir o arquivo.

2. **Preencher o Login**:
   - Clica em coordenadas específicas para focar no campo de login.
   - Escreve o nome de usuário ('Noeme').

3. **Preencher a Senha**:
   - Clica em coordenadas específicas para focar no campo de senha.
   - Escreve a senha ('senha').

4. **Realizar Login**:
   - Clica nas coordenadas do botão de login para enviar as credenciais.

```python
# arquivo: bot.py

import pyautogui

pyautogui.PAUSE = 2

# Abrir a ferramenta no computador
pyautogui.press("win")
pyautogui.write("Login.xlsx")
pyautogui.press("backspace")
pyautogui.press('enter')

# Preencher o login
pyautogui.click(x=511, y=254)
pyautogui.write('Noeme')

# Preencher a senha
pyautogui.click(x=471, y=294)
pyautogui.write('senha')



# Clicar em fazer login
pyautogui.click(x=340, y=426)
pyautogui.click(x=340, y=426)
```
# Script para encontrar as coordenadas 
Este script ajuda a encontrar as coordenadas exatas para cliques. Ele imprime a posição atual do cursor após um atraso de 3 segundos.
```
# arquivo: encontrar_coordenadas.py

import pyautogui
import time

time.sleep(3)
print(pyautogui.position())
```
# Como executar 
1. Executar o Script para Encontrar Coordenadas:
   - Execute o script coordenadas.py para descobrir as coordenadas dos campos que você deseja automatizar.
   - Mova o cursor sobre o campo desejado e observe a posição exibida no terminal.
   ```
   python position.py
   ```
2. Atulizar coordenadas
   - Atualize o script automacao_login.py com as coordenadas corretas obtidas do script de coordenadas.
3. Executar o Script de Automação de Login:
   - xecute o script automacao_login.py para realizar a automação de login.
   ```
   python bot.py
   ```
# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar uma issue ou um pull request com melhorias ou correções.
   
