from abc import ABC, abstractmethod
import string


class IApplicationLogger(ABC):
    """
    The ApplicationLogger provides an interface for a LibGDX Application to
    log messages and exceptions. A default implementations is provided for
    each backend, custom implementations can be provided and set using
    IApplication.ApplicationLogger = ApplicationLogger
    """

    # Logs a message with a tag.
    @abstractmethod
    def log(self, tag: string, message: string):
        pass

    # Logs an error message with a tag.
    @abstractmethod
    def error(self, tag: string, message: string):
        pass

    # Logs a debug message with a tag.
    @abstractmethod
    def debug(self, tag: string, message: string):
        pass
