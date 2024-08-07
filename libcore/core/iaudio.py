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
from gdx.audio.iaudio_device import IAudioDevice
from gdx.audio.iaudio_recorder import IAudioRecorder
from gdx.audio.imusic import IMusic
from gdx.audio.isound import ISound
from gdx.files.file_handle import FileHandle


class IAudio(ABC):

    @abstractmethod
    def new_audio_device(self, sampling_rate: int, is_mono: bool) -> IAudioDevice:
        """
        Creates a new AudioDevice either in mono or stereo mode.
        The AudioDevice has to be disposed via its AudioDevice.dispose()
        method when it is no longer used.
        """
        pass

    @abstractmethod
    def new_audio_recorder(self, sampling_rate: int, is_mono: bool) -> IAudioRecorder:
        """
        Creates a new AudioRecorder. The AudioRecorder has
        to be disposed after it is no longer used.
        """
        pass

    @abstractmethod
    def new_sound(self, file_handle: FileHandle) -> ISound:
        """
        Creates a new Sound which is used to play back audio effects such as
        gun shots or explosions. The Sound's audio data is retrieved from the
        file specified via the FileHandle.
        Note that the complete audio data is loaded into RAM. You should
        therefore not load big audio files with this method. The current upper
        limit for decoded audio is 1 MB. Currently supported formats are WAV,
        MP3 and OGG. The Sound has to be disposed if it is no longer used via
        the Sound.dispose() method.
        """
        pass

    @abstractmethod
    def new_music(self, file_handle: FileHandle) -> IMusic:
        """
        Creates a new Music instance which is used to play back a music stream
        from a file. Currently supported formats are WAV, MP3 and OGG. The Music
        instance has to be disposed if it is no longer used via the Music.dispose()
        method.
        Music instances are automatically paused when ApplicationListener.pause()
        is called and resumed when ApplicationListener.resume() is called.
        """
        pass

