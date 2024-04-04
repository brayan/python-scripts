import pyautogui
import time

while True:
    time.sleep(10)

    pyautogui.click(631, 872)

    pyautogui.typewrite(".....")

    time.sleep(5)

    for _ in range(5):
        pyautogui.press("backspace")
    
    time.sleep(50)