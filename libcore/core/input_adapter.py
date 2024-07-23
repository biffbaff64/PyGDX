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
