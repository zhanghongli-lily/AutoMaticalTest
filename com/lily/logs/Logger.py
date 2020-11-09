import logging
from ..config.config import logPath
import time

class Logger(object):

    def __init__(self, level="debug"):
        self.logger = logging.getLogger()
        self.logger.setLevel(level=level)
        self.format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

    def getLogger(self):

        return self.logger

    def info(self):

        self.logger.info("info")
        print("console")

    def debug(self):
        self.logger.debug("debug")

    def warning(self):
        self.logger.warning("warning")

    def error(self):
        self.logger.error("error")

    def critical(self):
        self.logger.critical("critical")

    def console_log(self):
        log_sh = logging.StreamHandler()
        log_sh.setLevel(logging.DEBUG)
        log_sh.setFormatter(self, self.format)
        self.logger.addHandler(log_sh)

    def file_log(self):
        log_name = time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + ".log"
        log_fh = logging.FileHandler(logPath + log_name, mode="w")
        log_fh.setLevel(logging.DEBUG)
        log_fh.format(self, self.format)
        self.logger.addHandler(log_fh)
        # print("file")
