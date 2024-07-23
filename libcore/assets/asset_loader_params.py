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

from abc import abstractmethod
import string
from typing import Generic, TypeVar

from libcore.assets.asset_manager import AssetManager

T = TypeVar('T')


# -----------------------------------------------------------------------------
class AssetLoaderParameters:

    class ILoadedCallback:

        @abstractmethod
        def finished_loading(self, am: AssetManager, fn: string, t: Generic[T]):
            pass

    loaded_callback: ILoadedCallback = None


# -----------------------------------------------------------------------------
class DefaultLoadedCallbackInnerClass(AssetLoaderParameters.ILoadedCallback):

    ref_count: int

    def __init__(self, rc: int):
        self.ref_count = rc

    def finished_loading(self, am: AssetManager, fn: string, t: Generic[T]):
        am.set_ref_count(fn, self.ref_count)
