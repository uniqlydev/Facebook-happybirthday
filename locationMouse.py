import pyautogui as pg
import time

while True:
    cursorX, cursorY = pg.position()
    print(cursorX, cursorY)
    time.sleep(1)