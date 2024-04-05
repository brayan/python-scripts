import pyautogui
import time

while True:
    time.sleep(5)

    pyautogui.click(631, 872)

    time.sleep(2)

    pyautogui.typewrite("abcde")

    for _ in range(5):
        pyautogui.press("backspace")
    
    time.sleep(55)