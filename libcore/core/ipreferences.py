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

from abc import ABC, abstractmethod
import string


class IPreferences(ABC):
    @abstractmethod
    def put_boolean(self, key: string, val: bool):
        pass

    @abstractmethod
    def put_integer(self, key: string, val: int):
        pass

    @abstractmethod
    def put_float(self, key: string, val: float):
        pass

    @abstractmethod
    def put_string(self, key: string, val: string):
        pass

    @abstractmethod
    def get_boolean(self):
        pass

    @abstractmethod
    def get_integer(self):
        pass

    @abstractmethod
    def get_float(self):
        pass

    @abstractmethod
    def get_string(self):
        pass

    @abstractmethod
    def put_map(self, map):
        pass

    @abstractmethod
    def get_map(self):
        pass

    @abstractmethod
    def contains(self, key: string) -> bool:
        pass

    @abstractmethod
    def remove(self, key: string):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def flush(self):
        pass
