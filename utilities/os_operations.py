import subprocess
import time
from utilities.utility_logger import UtilityLogger


class OSOperations:
    class_path = "os_operations.OSOperations"
    ulogger = UtilityLogger()


    @classmethod
    def execute_shell_command(cls, structured_command):
        # Works in Windows and Linux
        try:
            return subprocess.check_output(structured_command, shell=True).decode('utf-8')
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> execute_shell_command -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+cls.class_path, str(e)))
