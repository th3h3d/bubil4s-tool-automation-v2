import configparser
from utilities.custom_logger import Logger
from utilities.utility_logger import UtilityLogger
import time


class ReadConfig:
    class_path = "read_configs.ReadConfig"
    ulogger = UtilityLogger()

    @classmethod
    def get_config(cls, directory, section, value):
        try:
            config = configparser.RawConfigParser()
            config.read(directory)
            return config.get(section, value)
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> get_config -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+cls.class_path, str(e)))

    @classmethod
    def get_all_settings(cls):
        """Get All Settings"""
        try:
            execution_settings = cls.get_config("./configuration/execution_config.ini", "SETTINGS", "_ENABLED_CONFIGS")
            tool_settings = cls.get_config("./configuration/tool_config.ini", "SETTINGS", "_ENABLED_CONFIGS")
            all_settings = dict()

            # Resolving Tool Settings
            for config in execution_settings.split("|"):
                all_settings[str(config)] = cls.get_config("./configuration/execution_config.ini", "SETTINGS", config)

            # Resolving Execution Settings
            for configs in tool_settings.split("|"):
                for config in cls.get_config("./configuration/tool_config.ini", "SETTINGS", configs).split("|"):
                    all_settings[str(config)] = cls.get_config("./configuration/tool_config.ini", "SETTINGS", config)

            _logger = Logger(logfile_location="./logging/logs/")
            all_settings["LOGGER"] = _logger

            return all_settings
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> get_all_settings -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+cls.class_path, str(e)))

    @classmethod
    def print_all_configs(cls):
        pass

