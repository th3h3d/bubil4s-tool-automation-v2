import time


class UtilityLogger:

    @classmethod
    def log_this(cls, err_log):
        fo = open("./utilities/logs/{}.log".format(time.strftime("%Y%m%d", time.localtime())), "a")
        fo.write(err_log)
        fo.close()
