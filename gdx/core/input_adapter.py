from gdx.core.iinput_processor import IInputProcessor


class InputAdapter(IInputProcessor):
    """
    An adapter class for IInputProcessor. You can derive from this and
    only override what you need.
    """

    def key_up(self, keycode: int) -> bool:
        return False

    def key_down(self, keycode: int) -> bool:
        return False

    def key_typed(self, character: int) -> bool:
        return False

    def mouse_moved(self, screenx: int, screeny: int) -> bool:
        return False

    def scrolled(self, amountx: float, amounty: float) -> bool:
        return False
