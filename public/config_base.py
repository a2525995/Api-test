# -*- coding: utf-8 -*-


from configparser import ConfigParser
import ast

class ConfigBase(object):
    def __init__(self, conf_file):
        """
        初始化
        :param conf_file:
        """
        self._config = ConfigParser()
        self._config.read(conf_file, encoding='utf-8')

    def __check_value(self, section, key):
        return self._config and self._config.has_option(section, key)

    def get_sections(self):
        return self._config.sections()

    def get_config(self, section, key, default=None):
        if self.__check_value(section, key):
            return self._config.get(section, key)
        else:
            return default

    def get_int(self, section, key, default=None):
        if self.__check_value(section, key):
            return int(self.get_config(section, key, default))
        else:
            return int(default)

    def get_items(self, section):
        return dict(self._config.items(section))

    def get_array(self, section, key):
        res = []
        if self.__check_value(section, key):
            res = ast.literal_eval(self.get_config(section, key))
        return res
