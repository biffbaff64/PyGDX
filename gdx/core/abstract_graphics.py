from abc import ABC

from gdx.core.igraphics import IGraphics


class AbstractGraphics(IGraphics, ABC):

    def get_raw_delta_time(self):
        return self.get_delta_time()

    def get_density(self):
        return self.getppix() / 160.0

    def get_back_buffer_scale(self):
        return self.get_back_buffer_width() / self.get_width()

