from gdx.core.iscreen import IScreen


class ScreenAdapter(IScreen):
    """
    Convenience implementation of the iscreen interface.
    Derive from this and implement only what you need.
    """

    def show(self):
        pass

    def hide(self):
        pass

    def render(self, delta_time: float):
        pass

    def resize(self, _width: int, _height: int):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def dispose(self):
        pass
