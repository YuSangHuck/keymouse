import logging
import os

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
def setup_logger(log_file='logs/application.log'):
    # 로그 디렉토리 생성
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 파일 핸들러 설정
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d - %(funcName)s()] - %(message)s')
    file_handler.setFormatter(file_formatter)

    # 핸들러 추가
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
