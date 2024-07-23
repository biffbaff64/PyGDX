from abc import ABC, abstractmethod
import string


class IClipboard(ABC):

    @abstractmethod
    def has_contents(self) -> bool:
        pass

    @abstractmethod
    def contents(self) -> string:
        pass
