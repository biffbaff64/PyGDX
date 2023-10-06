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

from gdx.graphics.icursor import Cursor
from gdx.graphics.displaymode import DisplayMode
from gdx.graphics.gl20 import GL20
from gdx.graphics.gl30 import GL30
from gdx.graphics.monitor import Monitor
from gdx.graphics.bufferformat import BufferFormat
from gdx.graphics.graphicstype import GraphicsType
from gdx.graphics.glutils.glversion import GLVersion


class IGraphics(ABC):

    # Returns whether OpenGLES 3.0 is available.
    # Ifit is you can get an instance of GL30 via GetGL30(self) to access
    # OpenGLES 3.0 functionality.Note that this functionality will
    # only be available if you instructed the Application instance
    # to use OpenGLES 3.0!
    @abstractmethod
    def is_gl30_available(self) -> bool:
        pass

    @abstractmethod
    def get_gl20(self) -> GL20:
        pass

    @abstractmethod
    def get_gl30(self) -> GL30:
        pass

    @abstractmethod
    def set_gl20(self, gl20):
        pass

    @abstractmethod
    def set_gl30(self, gl30):
        pass

    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass

    @abstractmethod
    def get_back_buffer_width(self) -> int:
        pass

    @abstractmethod
    def get_back_buffer_height(self) -> int:
        pass

    @abstractmethod
    def get_back_buffer_scale(self) -> float:
        pass

    @abstractmethod
    def get_safe_inset_left(self) -> int:
        pass

    @abstractmethod
    def get_safe_inset_top(self) -> int:
        pass

    @abstractmethod
    def get_safe_inset_bottom(self) -> int:
        pass

    @abstractmethod
    def get_safe_inset_right(self) -> int:
        pass

    @abstractmethod
    def get_frame_id(self) -> int:
        pass

    @abstractmethod
    def get_delta_time(self) -> float:
        pass

    @abstractmethod
    def get_frames_per_second(self) -> int:
        pass

    @abstractmethod
    def get_graphics_type(self) -> GraphicsType:
        pass

    @abstractmethod
    def get_glversion(self) -> GLVersion:
        pass

    @abstractmethod
    def getppix(self) -> float:
        pass

    @abstractmethod
    def getppiy(self) -> float:
        pass

    @abstractmethod
    def getppcx(self) -> float:
        pass

    @abstractmethod
    def getppcy(self) -> float:
        pass

    @abstractmethod
    def get_density(self) -> float:
        pass

    @abstractmethod
    def supports_display_mode_change(self) -> bool:
        pass

    @abstractmethod
    def get_primary_monitor(self) -> Monitor:
        pass

    @abstractmethod
    def get_monitor(self) -> Monitor:
        pass

    @abstractmethod
    def get_monitors(self) -> []:
        pass

    @abstractmethod
    def get_displaymodes(self, monitor ) -> []:
        pass

    @abstractmethod
    def get_displaymode(self, monitor ) -> DisplayMode:
        pass

    @abstractmethod
    def set_fullscreen_mode(self, display_mode ) -> bool:
        pass

    @abstractmethod
    def set_windowed_mode(self, width, height ) -> bool:
        pass

    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_undecorated(self, undecorated ):
        pass

    @abstractmethod
    def set_resizable(self, resizable ):
        pass

    @abstractmethod
    def set_vsync(self, vsync ):
        pass

    @abstractmethod
    def set_foreground_fps(self, fps ):
        pass

    @abstractmethod
    def get_buffer_format(self) -> BufferFormat:
        pass

    @abstractmethod
    def supports_extension(self, extension ) -> bool:
        pass

    @abstractmethod
    def set_continuous_rendering(self, is_continuous):
        pass

    @abstractmethod
    def is_continuous_rendering(self) -> bool:
        pass

    @abstractmethod
    def request_rendering(self):
        pass

    @abstractmethod
    def is_full_screen(self) -> bool:
        pass

    @abstractmethod
    def new_cursor(self, pixmap, x_hotspot, y_hotspot) -> Cursor:
        pass

    @abstractmethod
    def set_cursor(self, cursor):
        pass

    @abstractmethod
    def set_system_cursor(self, system_cursor):
        pass
