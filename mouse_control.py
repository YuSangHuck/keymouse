import pyautogui
import logging
from config import (
    MOUSE_VALUE_ADJUSTMENT,
    DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_UP
)

# 로거 설정
logger = logging.getLogger(__name__)

def move_mouse(direction=None, value=None):
    if direction == DIRECTION_LEFT:
        pyautogui.move(-value, 0)
    elif direction == DIRECTION_DOWN:
        pyautogui.move(0, value)
    elif direction == DIRECTION_UP:
        pyautogui.move(0, -value)
    elif direction == DIRECTION_RIGHT:
        pyautogui.move(value, 0)

def scroll_mouse(direction=None, value=None):
    if direction == DIRECTION_UP:
        pyautogui.scroll(-value)
    elif direction == DIRECTION_DOWN:
        pyautogui.scroll(value)

def click_mouse():
    pyautogui.click()
    logger.info("Mouse clicked")

def adjust_value_mouse(increase=True):
    global MOUSE_VALUE_ADJUSTMENT
    global mouse_move_value, mouse_scroll_value
    if increase:
        mouse_move_value += MOUSE_VALUE_ADJUSTMENT
        mouse_scroll_value += MOUSE_VALUE_ADJUSTMENT
    else:
        mouse_move_value = max(0, mouse_move_value - MOUSE_VALUE_ADJUSTMENT)
        mouse_scroll_value = max(0, mouse_scroll_value - MOUSE_VALUE_ADJUSTMENT)
    logger.info(f"Adjusted mouse_move_value to {mouse_move_value}, mouse_scroll_value to {mouse_scroll_value}")
