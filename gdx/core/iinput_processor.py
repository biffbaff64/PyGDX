from abc import ABC, abstractmethod


class IInputProcessor(ABC):

    @abstractmethod
    def key_down(self, keycode: int):
        """
        Called when a key is pressed.

        :param keycode: The key code, from iinput.keys
        :return: True if the input was processed
        """
        pass

    @abstractmethod
    def key_up(self, keycode: int):
        """
        Called when a key is released.

        :param keycode: The key code, from iinput.keys
        :return: True if the input was processed
        """
        pass

    @abstractmethod
    def key_typed(self, character: int):
        """
        Called when a key is typed.

        :param keycode: The key code, from iinput.keys
        :return: True if the input was processed
        """
        pass

    @abstractmethod
    def mouse_moved(self, screenx: int, screeny: int):
        pass

    @abstractmethod
    def scrolled(self, amountx: float, amounty: float):
        pass
