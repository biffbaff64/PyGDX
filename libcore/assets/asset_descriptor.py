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

import string
from typing import Generic, TypeVar

from libcore.assets.asset_loader_params import AssetLoaderParameters
from libcore.files.file_handle import FileHandle

# -----------------------------------------------------------------------------

T = TypeVar('T')


class AssetDescriptor(Generic[T]):
    type: Generic[T] = None
    file_path: string = ""
    parameters: AssetLoaderParameters = None
    file_info: FileHandle = None

    def to_string(self) -> string:
        return "path: " + self.file_path + "type: " + self.type.full_name
