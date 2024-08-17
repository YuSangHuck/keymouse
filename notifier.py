# notifier.py
from logger import logger_instance
from win10toast import ToastNotifier
from config import NOTIFIER_DEFAULT_DURATION

class SingletonNotifier:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonNotifier, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.toaster = ToastNotifier()
        pass

    def get_notifiler(self):
        return self

    def noti(self, title, message, duration=NOTIFIER_DEFAULT_DURATION):
        try:
            self.toaster.show_toast(title,
                                    message,
                                    icon_path="custom.ico", # NOTE 이거에 따라서 `pkg_resources.DistributionNotFound: The 'win10toast' distribution was not found and is required by the application` 뜬다
                                    duration=duration)
        except Exception as e:
            logger_instance.error(f"Notification error: {e}")

# notifier 인스턴스 생성
notifier_instance = SingletonNotifier().get_notifiler()