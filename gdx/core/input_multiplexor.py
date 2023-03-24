from gdx.core.iinput_processor import IInputProcessor
from gdx.utils.collections.snapshot_array import SnapshotArray


# An InputProcessor that delegates to an ordered list of other
# InputProcessors. Delegation for an event stops if a processor
# returns true, which indicates that the event was handled.
class InputMultiplexor(IInputProcessor):

    snapshot_array: SnapshotArray

    def key_up(self, keycode: int):
        pass

    def key_down(self, keycode: int):
        pass

    def key_typed(self, character: int):
        pass

    def mouse_moved(self, screenx: int, screeny: int):
        pass

    def scrolled(self, amountx: float, amounty: float):
        pass
