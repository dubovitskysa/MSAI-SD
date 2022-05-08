from abc import ABC, abstractmethod
from datetime import datetime


class ILogger(ABC):
    @abstractmethod
    def log_string(self, string_tolog: str) -> None:
        pass

    @classmethod
    def new_instance(cls):
        return cls

    def _gettimestamp(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class ConsoleLogger(ILogger):
    def __init__(self):
        pass

    def log_string(self, string_tolog: str) -> None:
        print(string_tolog)

    def __some_internal_method(self):
        print('some_internal_method')


class FileLogger(ILogger):
    __def_file_name = 'log.txt'

    def __init__(self, file_log_name):
        if file_log_name is None or len(file_log_name) == 0:
            file_log_name = self.__def_file_name

        self.file = open(file_log_name, 'a', encoding="utf-8")

    def log_string(self, string_tolog: str) -> None:
        self.file.write(f'[{self._gettimestamp()}] {string_tolog} \n')

    def __del__(self):
        self.file.close()
        # print ('--del__')


class Logger(ILogger):
    def __init__(self,  cls_=None, file_log_name=None):
        self.__console_logger = ConsoleLogger()
        self.__file_logger = FileLogger(file_log_name)

        self.__cls_name = ' _ '
        if cls_ is not None:
            self.__cls_name = type(cls_).__name__

    def log_string(self, string_tolog: str) -> None:
        self.__console_logger.log_string(f'{self.__cls_name}: {string_tolog}')
        self.__file_logger.log_string(f'{self.__cls_name}: {string_tolog}')
