import keyboard
from mode_manager import check_switch
from config import KEY_SWITCH, setup_logger

# 로거 설정
setup_logger()

if __name__ == "__main__":
    keyboard.add_hotkey(KEY_SWITCH, check_switch)
    keyboard.wait()
