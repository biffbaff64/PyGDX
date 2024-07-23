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
