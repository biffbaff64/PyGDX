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

from gdx.graphics.igl20 import IGL20
from gdx.graphics.igl30 import IGL30
from gdx.core.igraphics import IGraphics
from gdx.core.iapplication import IApplication
from gdx.core.iaudio import IAudio
from gdx.core.ifiles import IFiles
from gdx.core.iinput import IInput


class Gdx:
    """
    Environment class holding references to the Application,
    Graphics, Audio, Files and Input instances.
    """
    # @formatter:off
    application     = IApplication()
    graphics        = IGraphics()
    audio           = IAudio()
    input           = IInput()
    files           = IFiles()
    gl              = IGL20()
    gl20            = IGL20()
    gl30            = IGL30()
    # @formatter:on

    # Test mode flag which, when TRUE, means that all developer options are enabled.
    # This must, however, mean that software with this enabled cannot be published.
    is_dev_mode: bool

    # From Wiktionary...
    # "1. (video games) A game mode where the player character is invulnerable to
    # damage, typically activated by entering a cheat code."
    # "2. (video games) A mode of play in (mostly) roguelike games, allowing the
    # player to create objects on demand, to be resurrected in the case of death, etc."
    # Note: Only the flag is provided by this library. It is intended for use in your
    # local game code.
    is_god_mode: bool
