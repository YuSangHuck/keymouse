import keyboard
from mode_manager import check_switch
from config import KEY_SWITCH, PROGRAM_NAME
from logger import logger_instance, SingletonLogger
from notifier import notifier_instance

if __name__ == "__main__":
    notifier_instance.noti(PROGRAM_NAME, "start")

    startup_log = (
"################################################################################\n"
"#                               Program started                                #\n"
"################################################################################"
)
    SingletonLogger().plain(startup_log)

    keyboard.add_hotkey(KEY_SWITCH, check_switch)
    keyboard.wait()
