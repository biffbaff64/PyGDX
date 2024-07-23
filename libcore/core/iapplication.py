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

from abc import ABC, abstractmethod
from enum import Enum
from gdx.core.ipreferences import IPreferences
import string
import re


class ApplicationType( Enum ):
    DesktopGL = 1
    WebGL = 2,
    Android = 3


class IApplication( ABC ):
    """
     An Application is the main entry point of your project. It sets up a window and
     rendering surface and manages the different aspects of your application, namely
     Graphics, Audio, Input and Files.
     This interface should be implemented in an application class for each supported
     backend.
     Each application class has its own startup and initialisation methods. Please
     refer to their documentation for more information.
     While game programmers are used to having a main loop, libgdx employs a different
     concept to accommodate the event based nature of Android applications a little more.
     Your application logic must be implemented in a ApplicationListener which has
     methods that get called by the Application when the application is created, resumed,
     paused, disposed or rendered. As a developer you will simply implement the
     ApplicationListener interface and fill in the functionality accordingly. The
     ApplicationListener is provided to a concrete Application instance as a parameter to
     the constructor or another initialisation method. Please refer to the documentation of
     the Application implementations for more information. Note that the ApplicationListener
     can be provided to any Application implementation. This means that you only need to write
     your program logic once and have it run on different platforms by passing it to a concrete
     Application implementation.
     The Application interface provides you with a set of modules for graphics, audio, input
     and file i/o.
     Graphics offers you various methods to output visuals to the screen. This is achieved via
     OpenGL ES 2.0 or 3.0 depending on what's available an the platform. On the desktop the features
     of OpenGL ES 2.0 and 3.0 are emulated via desktop OpenGL.
     Audio offers you various methods to output and record sound and music.
     Input offers you various methods to poll user input from the keyboard, touch screen, mouse
     and accelerometer. Additionally, you can implement an InputProcessor and use it with
     Input.setInputProcessor(InputProcessor) to receive input events.
     Files offers you various methods to access internal and external files. An internal file is
     a file that is stored near your application. On the desktop the classpath is first scanned for
     the specified file. If that fails then the root directory of your application is used for a
     lookup. External files are resources you create in your application and write to an external
     storage. On the desktop external files are written to a users home directory. If you know what
     you are doing you can also specify absolute file names. Absolute filenames are not portable,
     so take great care when using this feature.
     Net offers you various methods to perform network operations, such as performing HTTP requests,
     or creating server and client sockets for more elaborate network programming.
     The Application also has a set of methods that you can use to query specific information such
     as the operating system the application is currently running on and so forth. This allows you
     to have operating system dependent code paths. It is however not recommended to use these
     facilities.
     The Application also has a simple logging method which will print to standard out on the desktop.
    """

    # Log levels
    # LogNone will mute all log output.
    # LogError will only let error messages through.
    # LogInfo will let all non-debug messages through.
    # LogDebug will let all messages through.
    LogNone: int = 0
    LogInfo: int = 1
    LogDebug: int = 2
    LogError: int = 3

    log_level: int = LogNone
    is_running: bool = False

    @abstractmethod
    def log( self, message: string ):
        pass

    @abstractmethod
    def error( self, message: string ):
        pass

    @abstractmethod
    def debug( self, message: string ):
        pass

    @abstractmethod
    def get_application_type( self ) -> ApplicationType:
        pass

    @abstractmethod
    def get_preferences( self ) -> IPreferences:
        pass

    @abstractmethod
    def get_version( self ) -> int:
        pass

    @abstractmethod
    def add_lifecycle_listener( self, listener ):
        pass

    @abstractmethod
    def remove_lifecycle_listener( self, listener ):
        pass

    @abstractmethod
    def post_runnable( self, runnable ):
        pass

    @abstractmethod
    def exit( self ):
        pass
