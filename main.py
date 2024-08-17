import signal
import keyboard
import sys
from mode_manager import check_switch
from config import KEY_SWITCH
from logger import logger_instance, SingletonLogger

if __name__ == "__main__":
    startup_log = (
"################################################################################\n"
"#                               Program started                                #\n"
"################################################################################"
)
    SingletonLogger().plain(startup_log)

    keyboard.add_hotkey(KEY_SWITCH, check_switch)
    keyboard.wait()
