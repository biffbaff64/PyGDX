from gdx.graphics.gl20 import GL20
from gdx.graphics.gl30 import GL30
from igraphics import IGraphics
from iapplication import IApplication
from gdx.core.iaudio import IAudio
from gdx.core.ifiles import IFiles
from gdx.core.iinput import IInput


# Environment class holding references to the Application,
# Graphics, Audio, Files and Input instances.
class Gdx:
    # @formatter:off
    application     = IApplication()
    graphics        = IGraphics()
    audio           = IAudio()
    input           = IInput()
    files           = IFiles()
    gl              = GL20()
    gl20            = GL20()
    gl30            = GL30()
    # @formatter:on
