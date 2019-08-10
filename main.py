import pyautogui
import time
from mss import mss

start_x = 835
start_y = 700

bbox = (start_x, start_y, start_x + 300, start_y + 1)

cords_x = [0, 100, 200, 289]


def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pyautogui.click(1700, 1700)
        t2 = time.time()
        print(t2 - t1)


def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)


def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] < 20:
                    pyautogui.click(start_x + cord, start_y)
                    break


def start_debug():
    with mss() as sct:
        img = sct.grab(bbox)
        for cord in cords_x:
            print(img.pixel(cord, 0))

time.sleep(3)
#print_mouse_pos()
start()
#start_debug()
