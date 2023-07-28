import string

from gdx.core.iinput import IInput
from gdx.core.iinput_processor import IInputProcessor


class AbstractInput(IInput):
    #
    pressed_keys: [IInput.Keys.MaxKeycode + 1]
    just_pressed_keys: [IInput.Keys.MaxKeycode + 1]

    keys_to_catch: list
    pressed_keys_count: int
    key_just_pressed: bool

    # -----------------------------------------------------

    # -----------------------------------------------------

    def is_key_pressed(self, key: int) -> bool:
        if key == IInput.Keys.Any_Key: return self.pressed_keys_count > 0
        if key < 0 or key > IInput.Keys.MaxKeycode: return False
        return self.pressed_keys[key]

    def is_key_just_pressed(self, key: int):
        if key == IInput.Keys.Any_Key: return self.key_just_pressed
        if key < 0 or key > IInput.Keys.MaxKeycode: return False
        return self.just_pressed_keys[key]

    def get_text_input(self, listener: IInput.ITextInputListener, title: string, text: string, hint: string):
        pass

    def set_input_processor(self, processor: IInputProcessor):
        pass

    def get_input_processor(self) -> IInputProcessor:
        pass

    def get_accelerometer_x(self):
        pass

    def get_accelerometer_y(self):
        pass

    def get_accelerometer_z(self):
        pass

    def get_gyroscope_x(self):
        pass

    def get_gyroscope_y(self):
        pass

    def get_gyroscope_z(self):
        pass

    def get_max_pointers(self):
        pass

    def get_x(self):
        pass

    def get_y(self):
        pass

    def get_delta_x(self):
        pass

    def get_delta_y(self):
        pass

    def is_touched(self):
        pass

    def just_touched(self):
        pass

    def is_button_pressed(self, key: int):
        pass

    def is_button_just_pressed(self, key: int):
        pass

    # -----------------------------------------------------
