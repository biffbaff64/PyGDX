from abc import ABC, abstractmethod


class IScreen(ABC):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def render(self, delta_time):
        pass

    @abstractmethod
    def resize(self, _width, _height):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def dispose(self):
        pass

