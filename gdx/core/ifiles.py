import string
from abc import ABC, abstractmethod
from enum import Enum

from gdx.files.file_handle import FileHandle


class IFiles:

    class FileType(Enum):
        # Path relative to the root of the classpath.
        # Classpath files are always readonly.
        ClassPath = 0

        # Path relative to the application's root directory. If the file is not
        # found, then the classpath is checked. Internal files are always readonly.
        Internal = 1

        # Path relative to the root of the home directory of the current user.
        External = 2

        # Path that is a fully qualified, absolute filesystem path.
        Absolute = 3

        # Path relative to the applications root directory.
        Local = 4

    # -----------------------------------------------------

    @abstractmethod
    def get_file_handle(self, path: string, handle: FileHandle):
        pass

    @abstractmethod
    def class_path(self) -> FileHandle:
        pass

    @abstractmethod
    def internal(self) -> FileHandle:
        pass

    @abstractmethod
    def external(self) -> FileHandle:
        pass

    @abstractmethod
    def absolute(self) -> FileHandle:
        pass

    @abstractmethod
    def local(self) -> FileHandle:
        pass

    @abstractmethod
    def get_external_storage_path(self) -> string:
        pass

    @abstractmethod
    def is_external_storage_available(self) -> bool:
        pass

    @abstractmethod
    def get_local_storage_path(self) -> string:
        pass

    @abstractmethod
    def is_local_storage_available(self) -> bool:
        pass
