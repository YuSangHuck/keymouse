import os
import logging

class SingletonLogger:
    _instance = None

    def __new__(cls, log_file='logs/application.log'):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance._init_logger(log_file)
        return cls._instance

    def _init_logger(self, log_file='logs/application.log'):
        # 로그 디렉토리 생성
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger('KeyMouseLogger')
        logger.setLevel(logging.DEBUG)

        # 파일 핸들러 설정
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('[%(asctime)s] [%(module).9s::%(funcName).9s:%(lineno).3d] [%(levelname).1s] %(message)s')
        file_handler.setFormatter(file_formatter)

        # 핸들러 추가
        logger.addHandler(file_handler)

        self.logger = logger

    def get_logger(self):
        return self.logger

# logger 인스턴스 생성
logger_instance = SingletonLogger().get_logger()