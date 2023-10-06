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

from abc import ABC

from gdx.core.igraphics import IGraphics


class AbstractGraphics(IGraphics, ABC):

    def get_raw_delta_time(self):
        return self.get_delta_time()

    def get_density(self):
        return self.getppix() / 160.0

    def get_back_buffer_scale(self):
        return self.get_back_buffer_width() / self.get_width()

