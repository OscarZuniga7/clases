# pip install pyautogui
# pip install pillow

import pyautogui
import time

def type_code(code, delay=0.1):
    for line in code.splitlines():
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        time.sleep(delay)

# Código de ejemplo a escribir
codigo = """
print("Hola, Mundo!")
for i in range(5):
    print(i)
"""

# Controla la velocidad de escritura con el parámetro `delay`
type_code(codigo, delay=0.2)
