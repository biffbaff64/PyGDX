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


class Align:
    """
    Provides bit flag constants for alignment
    """
    CENTER = 1 << 0
    TOP = 1 << 1
    BOTTOM = 1 << 2
    LEFT = 1 << 3
    RIGHT = 1 << 4

    TOP_LEFT = TOP | LEFT
    TOP_RIGHT = TOP | RIGHT
    BOTTOM_LEFT = BOTTOM | LEFT
    BOTTOM_RIGHT = BOTTOM | RIGHT

    def is_left(self, align: int):
        """
        Returns TRUE if the supplied position is aligned to the LEFT.
        :param align: The sample alignment to check
        :return: boolean
        """
        return align & self.LEFT

    def is_right(self, align: int):
        """
        Returns TRUE if the supplied position is aligned to the RIGHT.
        :param align: The sample alignment to check
        :return: boolean
        """
        return align & self.RIGHT

    def is_top(self, align: int):
        """
        Returns TRUE if the supplied position is aligned to the TOP.
        :param align: The sample alignment to check
        :return: boolean
        """
        return align & self.TOP

    def is_bottom(self, align: int):
        """
        Returns TRUE if the supplied position is aligned to the BOTTOM.
        :param align: The sample alignment to check
        :return: boolean
        """
        return align & self.BOTTOM

    def to_string(self, position: int):
        """
        Returns a string that represents the provided alignment.
        """
        s = "Alignment "

        if position & self.TOP:
            s.join(":[TOP]")

        if position & self.BOTTOM:
            s.join(":[BOTTOM]")

        if position & self.LEFT:
            s.join(":[LEFT]")

        if position & self.RIGHT:
            s.join(":[RIGHT]")
