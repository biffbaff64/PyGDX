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
