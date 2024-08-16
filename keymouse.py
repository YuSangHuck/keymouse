import logging
import pyautogui
import keyboard
import time

MODE_KEYBOARD = 'keyboard'
MODE_MOUSE = 'mouse'

KEY_SWITCH = 'caps lock'  # 모드 전환을 위한 키
KEY_SWITCH_TIME_WINDOW = 1  # 모드 전환을 위해 키를 검사할 시간(초)
KEY_SWITCH_REQUIRED_PRESSES = 2  # 모드 전환을 위해 필요한 키 입력 횟수
KEY_H = 'h'
KEY_J = 'j'
KEY_K = 'k'
KEY_L = 'l'
KEY_U = 'u'
KEY_I = 'i'
KEY_PLUS = '+'
KEY_MINUS = '-'
KEY_C = 'c'

DIRECTION_LEFT = 'left'
DIRECTION_DOWN = 'down'
DIRECTION_UP = 'up'
DIRECTION_RIGHT = 'right'

MOUSE_VALUE_ADJUSTMENT = 50

# 모드 전환 및 상태 표시
control_mode = MODE_KEYBOARD  # 초기 모드는 키보드 모드
key_switch_press_times = []
is_moving = False  # 마우스가 움직이고 있는지 확인하는 플래그
mouse_move_value = 30
mouse_scroll_value = 30
hotkeys = []

# 로거 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d - %(funcName)s()] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

def toggle_mode():
    global hotkeys
    global control_mode
    if control_mode == MODE_KEYBOARD:
        control_mode = MODE_MOUSE
        hotkeys.append(keyboard.add_hotkey(KEY_H, move_mouse, args=(DIRECTION_LEFT, mouse_move_value)))
        hotkeys.append(keyboard.add_hotkey(KEY_J, move_mouse, args=(DIRECTION_DOWN, mouse_move_value)))
        hotkeys.append(keyboard.add_hotkey(KEY_K, move_mouse, args=(DIRECTION_UP, mouse_move_value)))
        hotkeys.append(keyboard.add_hotkey(KEY_L, move_mouse, args=(DIRECTION_RIGHT, mouse_move_value)))
        hotkeys.append(keyboard.add_hotkey(KEY_I, scroll_mouse, args=(DIRECTION_DOWN, mouse_scroll_value)))
        hotkeys.append(keyboard.add_hotkey(KEY_U, scroll_mouse, args=(DIRECTION_UP, mouse_scroll_value)))
        hotkeys.append(keyboard.add_hotkey(KEY_PLUS, lambda: adjust_value_mouse(increase=True)))
        hotkeys.append(keyboard.add_hotkey(KEY_MINUS, lambda: adjust_value_mouse(increase=False)))
        hotkeys.append(keyboard.add_hotkey(KEY_C, click_mouse))
    else:
        control_mode = MODE_KEYBOARD
        for hotkey in hotkeys:
            keyboard.remove_hotkey(hotkey)
        hotkeys = []  # 핫키 목록 초기화
        logger.info("All hotkeys removed")

    logger.info(f"change mode to '{control_mode}'")

def check_switch():
    global key_switch_press_times
    current_time = time.time()
    # key_switch의 눌림 타이밍 기록
    key_switch_press_times.append(current_time)
    # key_switch_time_window 초 이내의 타이밍 기록만 유지
    key_switch_press_times = [t for t in key_switch_press_times if current_time - t <= KEY_SWITCH_TIME_WINDOW]
    # key_switch가 key_switch_time_window초 이내에 key_switch_required_presses번 눌렸는지 확인
    if len(key_switch_press_times) >= KEY_SWITCH_REQUIRED_PRESSES:
        toggle_mode()
        # 타이밍 기록 초기화
        key_switch_press_times = []
    logger.info(f"on_switch_key called. Press times: {key_switch_press_times}")

def move_mouse(direction=None, value=None):
    global is_moving
    if control_mode == MODE_MOUSE:
        if direction == DIRECTION_LEFT:
            pyautogui.move(-value, 0)
        elif direction == DIRECTION_DOWN:
            pyautogui.move(0, value)
        elif direction == DIRECTION_UP:
            pyautogui.move(0, -value)
        elif direction == DIRECTION_RIGHT:
            pyautogui.move(value, 0)
    is_moving = False

def scroll_mouse(direction=None, value=None):
    global is_moving
    if control_mode == MODE_MOUSE:
        if direction == DIRECTION_UP:
            pyautogui.scroll(-value)  # 아래로 스크롤
        elif direction == DIRECTION_DOWN:
            pyautogui.scroll(value) # 위로 스크롤
    is_moving = False

def click_mouse():
    if control_mode == MODE_MOUSE:
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

if __name__ == "__main__":
    keyboard.add_hotkey(KEY_SWITCH, check_switch)
    keyboard.wait()
