# ///////////////////////////////////////////////////////////////////////////////
# Copyright [2023] [Richard Ikin]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ///////////////////////////////////////////////////////////////////////////////

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
