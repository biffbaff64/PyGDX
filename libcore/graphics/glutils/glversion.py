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

import re

from enum import Enum
from gdx.core.iapplication import ApplicationType


class GLType(Enum):
    NONE = 0,
    OPENGL = 1,
    GLES = 2,
    WEBGL = 3,

    # --------------------------------------
    VULKAN = 4,

    # --------------------------------------
    # Sub-Categories for OpenGL
    GL10 = 5,
    GL20 = 6,
    GL30 = 7,
    GL40 = 8


class GLVersion:
    vendor_string: str
    renderer_string: str
    gl_type: GLType

    def __init__(self, app: ApplicationType, version: str, vendor: str, renderer: str):
        self.determine_gl_type(app, version, vendor, renderer)

    def determine_gl_type(self, app_type, version_string, vendor_string, renderer_string):
        gl_type = {
            ApplicationType.Android  : GLType.GLES,
            ApplicationType.DesktopGL: GLType.OPENGL,
            ApplicationType.WebGL    : GLType.WEBGL
            }.get(app_type, GLType.NONE)

        major_version, minor_version, revision_version = -1, -1, -1

        if gl_type == GLType.GLES:
            pattern = r"OpenGL ES (\d(\.\d){0,2})"
            major_version, minor_version, revision_version = self.extract_version(pattern, version_string)
        elif gl_type == GLType.WEBGL:
            pattern = r"WebGL (\d(\.\d){0,2})"
            major_version, minor_version, revision_version = self.extract_version(pattern, version_string)
        elif gl_type == GLType.OPENGL:
            pattern = r"(\d(\.\d){0,2})"
            major_version, minor_version, revision_version = self.extract_version(pattern, version_string)

        return {
            "gl_type"         : gl_type,
            "major_version"   : major_version,
            "minor_version"   : minor_version,
            "revision_version": revision_version,
            "vendor_string"   : vendor_string,
            "renderer_string" : renderer_string
            }

    @staticmethod
    def extract_version(pattern: str, version_string: str):
        match = re.search(pattern, version_string)
        if match:
            version = match.group(1)
            return [int(x) for x in version.split('.')]
        return [-1, -1, -1]
