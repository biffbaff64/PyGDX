from abc import ABC, abstractmethod
import string


class IApplicationLogger(ABC):

    @abstractmethod
    def log(self, tag: string, message: string):
        pass

    @abstractmethod
    def error(self, tag: string, message: string):
        pass

    @abstractmethod
    def debug(self, tag: string, message: string):
        pass
