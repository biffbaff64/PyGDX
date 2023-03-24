from abc import ABC, abstractmethod


class IInputProcessor(ABC):

    @abstractmethod
    def key_up(self, keycode: int):
        pass

    @abstractmethod
    def key_down(self, keycode: int):
        pass

    @abstractmethod
    def key_typed(self, character: int):
        pass

    @abstractmethod
    def mouse_moved(self, screenx: int, screeny: int):
        pass

    @abstractmethod
    def scrolled(self, amountx: float, amounty: float):
        pass
