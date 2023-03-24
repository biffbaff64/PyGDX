from abc import ABC, abstractmethod
import string


class IPreferences(ABC):
    @abstractmethod
    def put_boolean(self, key: string, val: bool):
        pass

    @abstractmethod
    def put_integer(self, key: string, val: int):
        pass

    @abstractmethod
    def put_float(self, key: string, val: float):
        pass

    @abstractmethod
    def put_string(self, key: string, val: string):
        pass

    @abstractmethod
    def get_boolean(self):
        pass

    @abstractmethod
    def get_integer(self):
        pass

    @abstractmethod
    def get_float(self):
        pass

    @abstractmethod
    def get_string(self):
        pass

    @abstractmethod
    def put_map(self, map):
        pass

    @abstractmethod
    def get_map(self):
        pass

    @abstractmethod
    def contains(self, key: string) -> bool:
        pass

    @abstractmethod
    def remove(self, key: string):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def flush(self):
        pass
