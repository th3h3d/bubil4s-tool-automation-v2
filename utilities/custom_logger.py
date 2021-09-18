import logging
import time
from utilities.utility_logger import UtilityLogger


class Logger:

    def __init__(self, logfile_location=".\\", logfile_name=time.strftime("%Y%m%d", time.localtime()),
                 logfile_extension=".log", log_format='%(asctime)s - [%(levelname)s] - %(message)s'):
        """Set mandatory input.
        """
        self.logger = logging.getLogger('')  # get root handler for preparing
        file_handler = logging.FileHandler(logfile_location + str(logfile_name) + logfile_extension)
        file_handler.setFormatter(logging.Formatter(log_format))
        self.logger.addHandler(file_handler)
        self.class_path = "custom_logger.warning"
        self.ulogger = UtilityLogger()

    def warning(self, message):
        """This method is used to create a log for warning type.
        """
        try:
            self.logger.setLevel(logging.WARNING)
            self.logger.warning(message)
        except Exception as e:
            # Manual logger for logging
            self.ulogger.log_this("{} -> warning -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+self.class_path, str(e)))

    def info(self, message):
        """This method is used to create a log for info type.
        """
        try:
            self.logger.setLevel(logging.INFO)
            self.logger.info(message)
        except Exception as e:
            # Manual logger for logging
            self.ulogger.log_this("{} -> info -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+self.class_path, str(e)))

    def error(self, message):
        """This method is used to create a log for error type.
        """
        try:
            self.logger.setLevel(logging.ERROR)
            self.logger.error(message)
        except Exception as e:
            # Manual logger for logging
            self.ulogger.log_this("{} -> error -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+self.class_path, str(e)))

