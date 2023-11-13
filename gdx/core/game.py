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

from gdx.core.iapplication_listener import IApplicationListener
from gdx.core.iscreen import IScreen
from gdx.core.gdxapp import Gdx


# AnApplicationListener that delegates to a Screen. This allows an application
# to easily have multiple screens. Screens are not disposed automatically. You
# must handle whether you want to keep screens around or dispose of them when
# another screen is set.
class Game(IApplicationListener):
    screen = IScreen()

    # ---------------------------------
    def get_screen(self):
        return self.screen

    # ---------------------------------
    # Sets the current screen.Screen.hide() is called on any old screen,
    # and Screen.show() is called on the new screen, if any.
    def set_screen(self, _screen: IScreen):

        if self.screen is not None:
            self.screen.hide()

        screen = _screen

        if screen is not None:
            screen.show()

            if Gdx.graphics is not None:
                screen.resize(Gdx.graphics.get_width(), Gdx.graphics.get_height())

    # ---------------------------------
    def create(self):
        pass

    # ---------------------------------
    # Draw the current scene
    def render(self, delta_time):
        if Gdx.graphics is not None:
            self.screen.render(delta_time)

    # ---------------------------------
    def resize(self, _width, _height):
        self.screen.resize(_width, _height)

    # ---------------------------------
    def pause(self):
        self.screen.pause()

    # ---------------------------------
    def resume(self):
        self.screen.resume()

    # ---------------------------------
    def dispose(self):
        self.screen.dispose()

