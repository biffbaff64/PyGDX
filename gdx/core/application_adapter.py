from gdx.core.iapplication_listener import IApplicationListener


class ApplicationAdapter(IApplicationListener):
    """
    Convenience implementation of IApplicationListener.
    Derive from this and only override what you need.
    """

    def create(self):
        pass

    def render(self, delta_time: float):
        pass

    def resize(self, width: int, height: int):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def dispose(self):
        pass

