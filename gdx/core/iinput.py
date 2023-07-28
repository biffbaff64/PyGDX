import string
from enum import Enum
from abc import ABC, abstractmethod

from gdx.core.iinput_processor import IInputProcessor


# Interface to the input facilities.
# This allows polling the state of the keyboard, the touch screen and
# the accelerometer. On some backends (desktop, gwt, etc.) the touch
# screen is replaced by mouse input. The accelerometer is of course
# not available on all backends. Instead of polling for events, one
# can process all input events with an InputProcessor.
# You can set the InputProcessor via the SetInputProcessor(InputProcessor)
# method. It will be called before the ApplicationListener.render() method
# in each frame.
# Keyboard keys are translated to the constants in Input.Keys transparently
# on all systems. Do not use system specific key constants. The class also
# offers methods to use (and test for the presence of) other input systems
# like vibration, compass, on-screen keyboards, and cursor capture.
# Support for simple input dialogs is also provided.
class IInput(ABC):
    # -------------------------------------------
    # Mouse Buttons
    class Buttons:
        # @formatter:off
        Left:       int = 0
        Right:      int = 1
        Middle:     int = 2
        Back:       int = 3
        Forward:    int = 4
        # @formatter:on

    # -------------------------------------------
    class Keys:
        # @formatter:off
        Any_Key:                int = -1
        Num_0:                  int = 7
        Num_1:                  int = 8
        Num_2:                  int = 9
        Num_3:                  int = 10
        Num_4:                  int = 11
        Num_5:                  int = 12
        Num_6:                  int = 13
        Num_7:                  int = 14
        Num_8:                  int = 15
        Num_9:                  int = 16
        A:                      int = 29
        Alt_Left:               int = 57
        Alt_Right:              int = 58
        Apostrophe:             int = 75
        At:                     int = 77
        B:                      int = 30
        Back:                   int = 4
        BackSlash:              int = 73
        C:                      int = 31
        Call:                   int = 5
        Camera:                 int = 27
        Caps_Lock:              int = 115
        Clear:                  int = 28
        Comma:                  int = 55
        D:                      int = 32
        Del:                    int = 67
        Backspace:              int = 67
        Forward_Del:            int = 112
        Dpad_Center:            int = 23
        Dpad_Down:              int = 20
        Dpad_Left:              int = 21
        Dpad_Right:             int = 22
        Dpad_Up:                int = 19
        Center:                 int = 23
        Down:                   int = 20
        Left:                   int = 21
        Right:                  int = 22
        Up:                     int = 19
        E:                      int = 33
        Endcall:                int = 6
        Enter:                  int = 66
        Envelope:               int = 65
        Equals_Sign:            int = 70
        Explorer:               int = 64
        F:                      int = 34
        Focus:                  int = 80
        G:                      int = 35
        Grave:                  int = 68
        H:                      int = 36
        Headsethook:            int = 79
        Home:                   int = 3
        I:                      int = 37
        J:                      int = 38
        K:                      int = 39
        L:                      int = 40
        Left_Bracket:           int = 71
        M:                      int = 41
        Media_Fast_Forward:     int = 90
        Media_Next:             int = 87
        Media_Play_Pause:       int = 85
        Media_Previous:         int = 88
        Media_Rewind:           int = 89
        Media_Stop:             int = 86
        Menu:                   int = 82
        Minus:                  int = 69
        Mute:                   int = 91
        N:                      int = 42
        Notification:           int = 83
        Num:                    int = 78
        O:                      int = 43
        P:                      int = 44
        Pause:                  int = 121
        Period:                 int = 56
        Plus:                   int = 81
        Pound:                  int = 18
        Power:                  int = 26
        Print_Screen:           int = 120
        Q:                      int = 45
        R:                      int = 46
        Right_Bracket:          int = 72
        S:                      int = 47
        Scroll_Lock:            int = 116
        Search:                 int = 84
        Semicolon:              int = 74
        Shift_Left:             int = 59
        Shift_Right:            int = 60
        Slash:                  int = 76
        Soft_Left:              int = 1
        Soft_Right:             int = 2
        Space:                  int = 62
        Star:                   int = 17
        Sym:                    int = 63
        T:                      int = 48
        Tab:                    int = 61
        U:                      int = 49
        Unknown:                int = 0
        V:                      int = 50
        Volume_Down:            int = 25
        Volume_Up:              int = 24
        W:                      int = 51
        X:                      int = 52
        Y:                      int = 53
        Z:                      int = 54
        Meta_Alt_Left_On:       int = 16
        Meta_Alt_On:            int = 2
        Meta_Alt_Right_On:      int = 32
        Meta_Shift_Left_On:     int = 64
        Meta_Shift_On:          int = 1
        Meta_Shift_Right_On:    int = 128
        Meta_Sym_On:            int = 4
        Control_Left:           int = 129
        Control_Right:          int = 130
        Escape:                 int = 111
        End:                    int = 123
        Insert:                 int = 124
        Page_Up:                int = 92
        Page_Down:              int = 93
        Pictsymbols:            int = 94
        Switch_Charset:         int = 95
        Button_Circle:          int = 255
        Button_A:               int = 96
        Button_B:               int = 97
        Button_C:               int = 98
        Button_X:               int = 99
        Button_Y:               int = 100
        Button_Z:               int = 101
        Button_L1:              int = 102
        Button_R1:              int = 103
        Button_L2:              int = 104
        Button_R2:              int = 105
        Button_Thumbl:          int = 106
        Button_Thumbr:          int = 107
        Button_Start:           int = 108
        Button_Select:          int = 109
        Button_Mode:            int = 110
        # @formatter:on

        # @formatter:off
        Numpad_0:   int = 144
        Numpad_1:   int = 145
        Numpad_2:   int = 146
        Numpad_3:   int = 147
        Numpad_4:   int = 148
        Numpad_5:   int = 149
        Numpad_6:   int = 150
        Numpad_7:   int = 151
        Numpad_8:   int = 152
        Numpad_9:   int = 153

        Numpad_Divide:          int = 154
        Numpad_Multiply:        int = 155
        Numpad_Subtract:        int = 156
        Numpad_Add:             int = 157
        Numpad_Dot:             int = 158
        Numpad_Comma:           int = 159
        Numpad_Enter:           int = 160
        Numpad_Equals:          int = 161
        Numpad_Left_Paren:      int = 162
        Numpad_Right_Paren:     int = 163
        Num_Lock:               int = 143
        # @formatter:on

        # @formatter:off
        Colon:  int = 243
        F1:     int = 131
        F2:     int = 132
        F3:     int = 133
        F4:     int = 134
        F5:     int = 135
        F6:     int = 136
        F7:     int = 137
        F8:     int = 138
        F9:     int = 139
        F10:    int = 140
        F11:    int = 141
        F12:    int = 142
        F13:    int = 183
        F14:    int = 184
        F15:    int = 185
        F16:    int = 186
        F17:    int = 187
        F18:    int = 188
        F19:    int = 189
        F20:    int = 190
        F21:    int = 191
        F22:    int = 192
        F23:    int = 193
        F24:    int = 194

        MaxKeycode: int = 255
        # @formatter:on

    # -------------------------------------------
    @staticmethod
    def to_string(keycode: int):
        if keycode < 0:
            raise Exception("Keycode < 0 provided!")

        if keycode > IInput.Keys.MaxKeycode:
            raise Exception("Keycode > MaxKeyCode provided!")

        return ""

    # -------------------------------------------
    class ITextInputListener(ABC):
        @abstractmethod
        def input(self, text: string):
            pass

        @abstractmethod
        def cancelled(self):
            pass

    # -------------------------------------------
    # @formatter:off
    class Peripheral(Enum):
        HardwareKeyboard    = 0
        OnscreenKeyboard    = 1
        MultitouchScreen    = 2
        Accelerometer       = 3
        Compass             = 4
        Vibrator            = 5
        Gyroscope           = 6
        RotationVector      = 7
        Pressure            = 8
    # @formatter:on

    # -------------------------------------------
    # @formatter:off
    class OnscreenKeyboardType(Enum):
        Default     = 0
        NumberPad   = 1
        PhonePad    = 2
        Email       = 3
        Password    = 4
        Uri         = 5
    # @formatter:on

    # -------------------------------------------
    # @formatter:off
    class Orientation(Enum):
        Landscape   = 0
        Portrait    = 1
    # @formatter:on

    # -------------------------------------------
    # Abstract methods for child classes
    @abstractmethod
    def is_touched(self):
        pass

    @abstractmethod
    def just_touched(self):
        pass

    @abstractmethod
    def is_button_pressed(self, key: int):
        pass

    @abstractmethod
    def is_button_just_pressed(self, key: int):
        pass

    @abstractmethod
    def is_key_pressed(self, key: int):
        pass

    @abstractmethod
    def is_key_just_pressed(self, key: int):
        pass

    @abstractmethod
    def get_text_input(self, listener: ITextInputListener, title: string, text: string, hint: string):
        pass

    @abstractmethod
    def set_input_processor(self, processor: IInputProcessor):
        pass

    @abstractmethod
    def get_input_processor(self) -> IInputProcessor:
        pass

    # -------------------------------------------
    @abstractmethod
    def get_accelerometer_x(self):
        pass

    @abstractmethod
    def get_accelerometer_y(self):
        pass

    @abstractmethod
    def get_accelerometer_z(self):
        pass

    @abstractmethod
    def get_gyroscope_x(self):
        pass

    @abstractmethod
    def get_gyroscope_y(self):
        pass

    @abstractmethod
    def get_gyroscope_z(self):
        pass

    @abstractmethod
    def get_max_pointers(self):
        pass

    @abstractmethod
    def get_x(self):
        pass

    @abstractmethod
    def get_y(self):
        pass

    @abstractmethod
    def get_delta_x(self):
        pass

    @abstractmethod
    def get_delta_y(self):
        pass



