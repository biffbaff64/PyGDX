from gdx.core.iinput import IInput


class AbstractInput(IInput):
    #
    pressed_keys: [IInput.Keys.MaxKeycode + 1]
    just_pressed_keys: [IInput.Keys.MaxKeycode + 1]

    keys_to_catch: list
    pressed_keys_count: int
    key_just_pressed: bool

    # -----------------------------------------------------


    # -----------------------------------------------------

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
