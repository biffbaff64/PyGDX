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
from gdx.core.iinput import IInput
from gdx.core.iinput_processor import IInputProcessor


class AbstractInput(ABC, IInput):
    #
    pressed_keys: [IInput.Keys.MaxKeycode + 1]
    just_pressed_keys: [IInput.Keys.MaxKeycode + 1]

    keys_to_catch: list
    pressed_keys_count: int
    key_just_pressed: bool

    # -----------------------------------------------------

    # -----------------------------------------------------

    # -------------------------------------------------------------------------
    def is_key_pressed(self, key: int) -> bool:
        """
        Returns TRUE if the specified key is currently pressed.
        """
        if key == IInput.Keys.Any_Key:
            return self.pressed_keys_count > 0

        if key < 0 or key > IInput.Keys.MaxKeycode:
            return False

        return self.pressed_keys[key]

    # -------------------------------------------------------------------------
    def is_key_just_pressed(self, key: int) -> bool:
        """
        Returns TRUE if the specified key has just been pressed.
        """
        if key == IInput.Keys.Any_Key:
            return self.key_just_pressed

        if key < 0 or key > IInput.Keys.MaxKeycode:
            return False

        return self.just_pressed_keys[key]

    # -------------------------------------------------------------------------
    def is_catch_back_key(self) -> bool:
        return self.keys_to_catch.__contains__(IInput.Keys.Back)

    # -------------------------------------------------------------------------
    def set_catch_back_key(self, catch: bool):
        self.set_catch_key(IInput.Keys.Back, catch)

    # -------------------------------------------------------------------------
    def is_catch_menu_key(self) -> bool:
        return self.keys_to_catch.__contains__(IInput.Keys.Menu)

    # -------------------------------------------------------------------------
    def set_catch_menu_key(self, catch: bool):
        self.set_catch_key(IInput.Keys.Menu, catch)

    # -------------------------------------------------------------------------
    def set_catch_key(self, keycode: int, catchkey: bool):
        """
        If 'catchkey' is TRUE the supplied keycode is added to 'keys_to_catch'.
        If 'catchkey' is FALSE the supplied keycode is removed from 'keys_to_catch'.
        """
        if catchkey:
            self.keys_to_catch.append(keycode)
        else:
            self.keys_to_catch.remove(keycode)

    # -------------------------------------------------------------------------
    def is_catch_key(self, keycode: int) -> bool:
        """
        Returns TRUE if the specified keycode is a member
        of the 'keys_to_catch' list.
        """
        return self.keys_to_catch.__contains__(keycode)

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_text_input(self, listener: IInput.ITextInputListener, title: string, text: string, hint: string):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def set_input_processor(self, processor: IInputProcessor):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_input_processor(self) -> IInputProcessor:
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_accelerometer_x(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_accelerometer_y(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_accelerometer_z(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_gyroscope_x(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_gyroscope_y(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_gyroscope_z(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_max_pointers(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_x(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_y(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_delta_x(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def get_delta_y(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def is_touched(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def just_touched(self):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def is_button_pressed(self, key: int):
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def is_button_just_pressed(self, key: int):
        pass

    # -------------------------------------------------------------------------
