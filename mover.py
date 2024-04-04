import pyautogui
import random
import time


MIN_POSITION = 10
MAX_POSITION = 100
INTERVAL_IN_SECONDS = 60


def get_random_position(current_position):
    should_add = random.choice([True, False])
    random_position = random.randint(MIN_POSITION, MAX_POSITION)

    if should_add:
        return random_position + current_position
    else:
        return random_position - current_position


def print_local_time():
    current_time = time.localtime()
    print(time.strftime("%H:%M:%S", current_time))


while True:
    print_local_time()

    x, y = pyautogui.position()
    
    pyautogui.moveTo(get_random_position(x), get_random_position(y))
    pyautogui.moveTo(x, y)
    
    time.sleep(INTERVAL_IN_SECONDS)