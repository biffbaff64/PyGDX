from abc import ABC, abstractmethod


class IApplicationListener(ABC):

    @abstractmethod
    def create(self):
        pass

    # Called when the application should render itself
    @abstractmethod
    def render(self, delta_time: float):
        pass

    # Called when the application is resized.
    @abstractmethod
    def resize(self, width: int, height: int):
        pass

    # Called when the application is paused, usually
    # when losing focus
    @abstractmethod
    def pause(self):
        pass

    # Called when the application is resumed from a paused
    # state, usually when regaining focus
    @abstractmethod
    def resume(self):
        pass

    # Called when the application is destroyed
    @abstractmethod
    def dispose(self):
        pass
