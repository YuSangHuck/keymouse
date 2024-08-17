import pyautogui
from logger import logger_instance
from config import (
    DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_UP
)

def move_mouse(direction=None, value=None):
    if direction == DIRECTION_LEFT:
        pyautogui.move(-value, 0)
    elif direction == DIRECTION_DOWN:
        pyautogui.move(0, value)
    elif direction == DIRECTION_UP:
        pyautogui.move(0, -value)
    elif direction == DIRECTION_RIGHT:
        pyautogui.move(value, 0)
    logger_instance.debug(f"direction: {direction}, value: {value}")

def scroll_mouse(direction=None, value=None):
    if direction == DIRECTION_UP:
        pyautogui.scroll(-value)
    elif direction == DIRECTION_DOWN:
        pyautogui.scroll(value)
    logger_instance.debug(f"direction: {direction}, value: {value}")

def click_mouse():
    pyautogui.click()
    logger_instance.info("Mouse clicked")
