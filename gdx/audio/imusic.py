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


class IMusic(ABC):

    @abstractmethod
    def play(self):
        """
        Starts the playback of the music stream. In case the stream was paused this
        will resume the playback. In case the music stream is finished playing this
        will restart the playback.
        """
        pass

    @abstractmethod
    def pause(self):
        """
        Pauses the playback. If the music stream has not been started yet or has
        finished playing a call to this method will be ignored.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stops a playing or paused Music instance. Next time play() is invoked
        the Music will start from the beginning.
        """
        pass

    @abstractmethod
    def is_playing(self):
        """
        whether this music stream is playing.
        """
        pass

    @abstractmethod
    def set_looping(self, is_looping):
        """
        Sets whether the music stream is looping. This can be called at any
        time, whether the stream is playing or not.
        """
        pass

    @abstractmethod
    def is_looping(self):
        """
        Whether the music stream is set to loop or not.
        """
        pass

    @abstractmethod
    def set_volume(self, volume):
        """
        Sets the volume of this music stream. The volume must be given
        in the range [0,1] with 0 being silent and 1 being the maximum
        volume.
        """
        pass

    @abstractmethod
    def get_volume(self):
        """
        the volume of this music stream.
        """
        pass

    @abstractmethod
    def set_pan(self, pan, volume):
        """
        Sets the panning and volume of this music stream.
        :param pan: panning in the range -1 (full left) to 1 (full right). 0 is center position.
        :param volume: the volume in the range [0,1].
        :return:
        """
        pass

    @abstractmethod
    def set_position(self, position):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def dispose(self):
        pass

    @abstractmethod
    def set_on_completion_listener(self, listener):
        pass

    class IOnCompletionListener(ABC):

        @abstractmethod
        def on_completion(self, music):
            pass
