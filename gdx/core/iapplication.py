from abc import ABC, abstractmethod
from enum import Enum
from gdx.core.ipreferences import IPreferences
import string


class IApplication(ABC):
    #
    class ApplicationType(Enum):
        DesktopGL = 1
        WebGL = 2

    # Log levels
    LogNone: int = 0
    LogInfo: int = 1
    LogDebug: int = 2
    LogError: int = 3

    LogLevel: int = LogNone
    IsRunning: bool = False

    @abstractmethod
    def log(self, message: string):
        pass

    @abstractmethod
    def error(self, message: string):
        pass

    @abstractmethod
    def debug(self, message: string):
        pass

    @abstractmethod
    def get_application_type(self) -> ApplicationType:
        pass

    @abstractmethod
    def get_preferences(self) -> IPreferences:
        pass

    @abstractmethod
    def get_version(self) -> int:
        pass

    @abstractmethod
    def add_lifecycle_listener(self, listener):
        pass

    @abstractmethod
    def remove_lifecycle_listener(self, listener):
        pass

    @abstractmethod
    def exit(self):
        pass
