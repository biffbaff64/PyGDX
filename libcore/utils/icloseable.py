from abc import ABC, abstractmethod


class ICloseable(ABC):

    @abstractmethod
    def close(self):
        pass
