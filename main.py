import keyboard
from mode_manager import check_switch
from config import KEY_SWITCH

if __name__ == "__main__":
    keyboard.add_hotkey(KEY_SWITCH, check_switch)
    keyboard.wait()
