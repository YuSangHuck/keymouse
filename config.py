import logging

# 모드 상수
MODE_KEYBOARD = 'keyboard'
MODE_MOUSE = 'mouse'

# 핫키 및 타이밍 관련 상수
KEY_SWITCH = 'caps lock'
KEY_SWITCH_TIME_WINDOW = 1
KEY_SWITCH_REQUIRED_PRESSES = 2
KEY_H = 'h'
KEY_J = 'j'
KEY_K = 'k'
KEY_L = 'l'
KEY_U = 'u'
KEY_I = 'i'
KEY_PLUS = '+'
KEY_MINUS = '-'
KEY_C = 'c'

# 방향 상수
DIRECTION_LEFT = 'left'
DIRECTION_DOWN = 'down'
DIRECTION_UP = 'up'
DIRECTION_RIGHT = 'right'

# 마우스 값 조정
MOUSE_VALUE_ADJUSTMENT = 30
mouse_move_value = 30
mouse_scroll_value = 30

# 로거 설정
def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d - %(funcName)s()] - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
