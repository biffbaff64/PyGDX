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
