import keyboard
from mode_manager import check_switch
from config import KEY_SWITCH
from logger import logger_instance, SingletonLogger
from win10toast import ToastNotifier

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title,
                    message,
                    icon_path="custom.ico", # NOTE 이거에 따라서 `pkg_resources.DistributionNotFound: The 'win10toast' distribution was not found and is required by the application` 뜬다
                    duration=10)

if __name__ == "__main__":
    show_notification("Screenshot", "Screenshot saved to images folder.")

    startup_log = (
"################################################################################\n"
"#                               Program started                                #\n"
"################################################################################"
)
    SingletonLogger().plain(startup_log)

    keyboard.add_hotkey(KEY_SWITCH, check_switch)
    keyboard.wait()
