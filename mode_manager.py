import keyboard
from logger import logger_instance
import time
from mouse_control import move_mouse, scroll_mouse, click_mouse
from config import (
    MODE_KEYBOARD, MODE_MOUSE, KEY_SWITCH_TIME_WINDOW, KEY_SWITCH_REQUIRED_PRESSES,
    KEY_H, KEY_J, KEY_K, KEY_L, KEY_U, KEY_I, KEY_C, KEY_CTRL,
    DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_UP,
    MOUSE_MOVE_VALUE_BIG, MOUSE_MOVE_VALUE_SMALL, MOUSE_SCROLL_VALUE_BIG, MOUSE_SCROLL_VALUE_SMALL
)

# 모드 및 핫키 관리
control_mode = MODE_KEYBOARD
key_switch_press_times = []
hotkeys = []

def toggle_mode():
    global hotkeys
    global control_mode
    if control_mode == MODE_KEYBOARD:
        control_mode = MODE_MOUSE
        hotkeys.append(keyboard.add_hotkey(KEY_H, move_mouse, args=(DIRECTION_LEFT, MOUSE_MOVE_VALUE_BIG)))
        hotkeys.append(keyboard.add_hotkey(KEY_J, move_mouse, args=(DIRECTION_DOWN, MOUSE_MOVE_VALUE_BIG)))
        hotkeys.append(keyboard.add_hotkey(KEY_K, move_mouse, args=(DIRECTION_UP, MOUSE_MOVE_VALUE_BIG)))
        hotkeys.append(keyboard.add_hotkey(KEY_L, move_mouse, args=(DIRECTION_RIGHT, MOUSE_MOVE_VALUE_BIG)))
        hotkeys.append(keyboard.add_hotkey(KEY_CTRL + '+' + KEY_H, move_mouse, args=(DIRECTION_LEFT, MOUSE_MOVE_VALUE_SMALL)))
        hotkeys.append(keyboard.add_hotkey(KEY_CTRL + '+' + KEY_J, move_mouse, args=(DIRECTION_DOWN, MOUSE_MOVE_VALUE_SMALL)))
        hotkeys.append(keyboard.add_hotkey(KEY_CTRL + '+' + KEY_K, move_mouse, args=(DIRECTION_UP, MOUSE_MOVE_VALUE_SMALL)))
        hotkeys.append(keyboard.add_hotkey(KEY_CTRL + '+' + KEY_L, move_mouse, args=(DIRECTION_RIGHT, MOUSE_MOVE_VALUE_SMALL)))
        hotkeys.append(keyboard.add_hotkey(KEY_I, scroll_mouse, args=(DIRECTION_DOWN, MOUSE_SCROLL_VALUE_BIG)))
        hotkeys.append(keyboard.add_hotkey(KEY_U, scroll_mouse, args=(DIRECTION_UP, MOUSE_SCROLL_VALUE_BIG)))
        hotkeys.append(keyboard.add_hotkey(KEY_CTRL + '+' + KEY_I, scroll_mouse, args=(DIRECTION_DOWN, MOUSE_SCROLL_VALUE_SMALL)))
        hotkeys.append(keyboard.add_hotkey(KEY_CTRL + '+' + KEY_U, scroll_mouse, args=(DIRECTION_UP, MOUSE_SCROLL_VALUE_SMALL)))
        hotkeys.append(keyboard.add_hotkey(KEY_C, click_mouse))
        logger_instance.debug("All hotkeys added")
    else:
        control_mode = MODE_KEYBOARD
        for hotkey in hotkeys:
            keyboard.remove_hotkey(hotkey)
        hotkeys = []  # 핫키 목록 초기화
        logger_instance.debug("All hotkeys removed")

    logger_instance.info(f"Change mode to '{control_mode}'")

def check_switch():
    global key_switch_press_times
    current_time = time.time()
    key_switch_press_times.append(current_time)
    key_switch_press_times = [t for t in key_switch_press_times if current_time - t <= KEY_SWITCH_TIME_WINDOW]
    if len(key_switch_press_times) >= KEY_SWITCH_REQUIRED_PRESSES:
        toggle_mode()
        key_switch_press_times = []
    logger_instance.debug(f"On switch key called. Press times: {key_switch_press_times}")
