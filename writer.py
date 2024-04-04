import pyautogui
import time

while True:
    time.sleep(5)

    pyautogui.click(631, 872)

    pyautogui.typewrite("A Elseeeee é uma toupeira...")

    time.sleep(5)

    for _ in range(28):
        pyautogui.press("backspace")
    
    time.sleep(5)