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

from gdx.graphics.glutils.glversion import GLVersion
from gdx.graphics.igl20 import IGL20
from gdx.graphics.igl30 import IGL30
from gdx.graphics.opengl.iglbindings import IGLBindings

from typing import List, Optional, Tuple


class BufferFormatDescriptor:

    def __init__(self, r: int, g: int, b: int, a: int, depth: int, stencil: int, samples: int, coverage_sampling: bool):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.depth = depth
        self.stencil = stencil
        self.samples = samples
        self.coverage_sampling = coverage_sampling

    def __str__(self):
        return f"r - {self.r}, g - {self.g}, b - {self.b}, a - {self.a}, depth - {self.depth}, stencil - {self.stencil}, num samples - {self.samples}, coverage sampling - {self.coverage_sampling}"


class DisplayMode:

    def __init__(self, width: int, height: int, refresh_rate: int, bits_per_pixel: int):
        self.width = width
        self.height = height
        self.refresh_rate = refresh_rate
        self.bits_per_pixel = bits_per_pixel

    def __str__(self):
        return f"{self.width}x{self.height}, bpp: {self.bits_per_pixel}, hz: {self.refresh_rate}"


class GdxMonitor:

    def __init__(self, x: int, y: int, name: Optional[str]):
        self.virtual_x = x
        self.virtual_y = y
        self.name = name


class IGraphics:

    back_buffer_width: int
    back_buffer_height: int
    logical_width: int
    logical_height: int
    gl20: IGL20
    gl30: IGL30
    delta_time: float
    gl_version: GLVersion
    continuous_rendering: bool

    def __init__(self):
        self.gl_version: Optional[GLVersion] = None
        self.graphics_type: Optional[GLType] = None
        self.buffer_format: Optional[BufferFormatDescriptor] = None
        self.gl: Optional[IGLBindings] = None
        self.delta_time: float = 0.0
        self.width: int = 0
        self.height: int = 0
        self.back_buffer_width: int = 0
        self.back_buffer_height: int = 0
        self.is_fullscreen: bool = False

    def get_raw_delta_time( self ):
        return self.delta_time

    def get_density( self ):
        return self.get_ppix() / 160.0

    def get_back_buffer_scale( self ):
        return self.back_buffer_width / self.width

    def is_gl30_available(self) -> bool:
        pass

    def get_safe_inset_left(self) -> int:
        pass

    def get_safe_inset_top(self) -> int:
        pass

    def get_safe_inset_bottom(self) -> int:
        pass

    def get_safe_inset_right(self) -> int:
        pass

    def get_frame_id(self) -> int:
        pass

    def get_frames_per_second(self) -> int:
        pass

    def get_ppc_xy(self) -> Tuple[float, float]:
        pass

    def get_ppi_xy(self) -> Tuple[float, float]:
        pass

    def get_ppix(self) -> float:
        pass

    def get_ppiy(self) -> float:
        pass

    def supports_display_mode_change(self) -> bool:
        pass

    def get_display_modes(self) -> List[DisplayMode]:
        pass

    def get_display_modes_for_monitor(self, gdx_monitor: GdxMonitor) -> List[DisplayMode]:
        pass

    def get_display_mode(self) -> DisplayMode:
        pass

    def get_display_mode_for_monitor(self, gdx_monitor: GdxMonitor) -> DisplayMode:
        pass

    def set_fullscreen_mode(self, display_mode: DisplayMode) -> bool:
        pass

    def set_windowed_mode(self, width: int, height: int) -> bool:
        pass

    def set_title(self, title: str):
        pass

    def set_undecorated(self, undecorated: bool):
        pass

    def set_resizable(self, resizable: bool):
        pass

    def set_vsync(self, vsync: bool):
        pass

    def set_foreground_fps(self, fps: int):
        pass

    def supports_extension(self, extension: str) -> bool:
        pass

    @property
    def continuous_rendering(self) -> bool:
        pass

    def request_rendering(self):
        pass
