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


class GdxVersion:
    version_string: string = "0.0.1"

    major: int = 0
    minor: int = 0
    revision: int = 1

    # -----------------------------------------------------

    def __init__(self):
        try:
            v: [3] = self.version_string.split("\\.")

            self.major = 0 if len(v) < 1 else int(v[0])
            self.major = 0 if len(v) < 2 else int(v[1])
            self.major = 0 if len(v) < 3 else int(v[2])

        except Exception:
            raise Exception("Invalid Version Number")

    # -----------------------------------------------------

    @staticmethod
    def is_higher(self, major: int, minor: int, revision: int):
        return self.is_higher_equal(self, major, minor, revision + 1)

    @staticmethod
    def is_lower(self, major: int, minor: int, revision: int):
        return self.is_lower_equal(self, major, minor, revision - 1)

    @staticmethod
    def is_higher_equal(self, major: int, minor: int, revision: int):
        if self.major != major:
            return self.major > major

        if self.minor != minor:
            return self.minor > minor

        return self.revision >= revision

    @staticmethod
    def is_lower_equal(self, major: int, minor: int, revision: int):
        if self.major != major:
            return self.major < major

        if self.minor != minor:
            return self.minor < minor

        return self.revision <= revision
