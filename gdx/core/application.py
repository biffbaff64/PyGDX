import string
from enum import Enum
from gdx.core.ipreferences import IPreferences


class Application:
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

    def log(self, message: string):
        pass

    def error(self, message: string):
        pass

    def debug(self, message: string):
        pass

    def get_application_type(self) -> ApplicationType:
        pass

    def get_preferences(self) -> IPreferences:
        pass

    def get_version(self) -> int:
        pass

    def add_lifecycle_listener(self, listener):
        pass

    def remove_lifecycle_listener(self, listener):
        pass

    def exit(self):
        pass
