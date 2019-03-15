import logging
from logging.handlers import RotatingFileHandler

class Log(object):
    def __init__(self, filename, level="INFO"):
        try:
            level = eval("logging." + level)
        except:
            raise Exception("Please Input <DEBUG|INFO|WARN|ERROR>")
        #切割路径，获取文件名
        name = str(filename).split('/')[-1]
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        formatter = logging.Formatter(fmt="[time:%(asctime)s - file:%(name)s] - %(levelname)s : %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        filehandler = RotatingFileHandler(filename, maxBytes=5 * 1024 * 1024, backupCount=5, mode='a')
        filehandler.setFormatter(formatter)
        self._logger.addHandler(filehandler)

        cmdhandler = logging.StreamHandler()
        cmdhandler.setFormatter(formatter)
        self._logger.addHandler(cmdhandler)

    def log_debug(self, msg):
        self._logger.debug(msg)

    def log_info(self, msg):
        self._logger.info(msg)

    def log_warn(self, msg):
        self._logger.warning(msg)

    def log_error(self, msg):
        self._logger.error(msg)

