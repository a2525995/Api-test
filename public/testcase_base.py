from public import utils
from public.logger import *
from public.config_base import *

class CaseBase(object):
    """
    每个testcase必须实例化这个类用来管理config和log
    """
    def  __init__(self, config=None, logger=None):
        """
        每个test_*.py在执行前会调用setup方法，将该类实例化
        :param config: 配置文件的类
        :param logger: 日志的类
        :return:
        """
        self._config = config
        self._logger = logger

    def end(self):
        """
        每个test_*.py在执行后会调用teardown方法，将对环境处理的事情清除
        :return:
        """
        self._config = None
        self._logger = None

    def get_sections(self):
        return self._config.get_sections()

    def get_config(self, section, key, default=None):
        return self._config.get_config(section, key, default)

    def get_int(self, section, key, default=None):
        return self._config.get_int(section, key, default)

    def get_items(self, section):
        return self._config.get_items(section)

    def get_array(self, section, key):
        return self._config.get_array(section, key)

    def log_debug(self, msg):
        self._logger.log_debug(msg)

    def log_info(self, msg):
        self._logger.log_info(msg)

    def log_warn(self, msg):
        self._logger.log_warn(msg)

    def log_error(self, msg):
        self._logger.log_error(msg)

    def log_exception(self, msg):
        self._logger.log_exception(msg)

