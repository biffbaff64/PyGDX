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
