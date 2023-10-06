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


class ISound(ABC):
    """
    A Sound is a short audio clip that can be played numerous times in parallel.
    It's completely loaded into memory so only load small audio files. Call the
    :func:'dispose()' method when you're done using the sound.
    Sound instances are created via a call to :func:'core.iaudio.new_sound(FileHandle)'
    Calling the {@link #play()} or {@link #play(float)} method will return a long
    which is an id to that instance of the sound. You can use this id to modify
    the playback of that sound instance.
    Note: any values provided will not be clamped. It is the responsibility of the
    developer to ensure values are correct.
    """

    @abstractmethod
    def play( self, volume: float = None, pitch: float = None, pan: float = None ) -> int:
        """
        Plays the sound. If the sound is already playing, it will be played again, concurrently.
        :param volume: the volume in the range [0,1] (optional)
        :param pitch: the pitch multiplier, 1 == default, greater than 1 == faster, less than 1 == slower,
                        the value has to be between '0.5' and '2.0' (optional)
        :param pan: panning in the range -1 (full left) to 1 (full right). 0 is center position. (optional)
        :return: the id of the sound instance if successful, or -1 on failure.
        """
        pass

    @abstractmethod
    def loop( self, volume: float = None, pitch: float = None, pan: float = None ):
        """
        Plays the sound, looping. If the sound is already playing,
        it will be played again, concurrently.
        :param volume: the volume in the range [0, 1] (optional)
        :param pitch: the pitch multiplier, 1 == default, greater than 1 == faster, less than 1 == slower,
                        the value has to be between '0.5' and '2.0' (optional)
        :param pan: panning in the range -1 (full left) to 1 (full right). 0 is center position. (optional)
        :return: the id of the sound instance if successful, or -1 on failure.
        """
        pass

    @abstractmethod
    def stop( self, sound_id: int = None ):
        """
        Stops playing all instances of this sound, or the specified sound id if supplied.
        If the sound is no longer playing, this has no effect.
        :param: the sound id (optional)
        :return:
        """
        pass

    @abstractmethod
    def pause( self, sound_id: int = None ):
        """
        Pauses all instances of this sound, or the specified sound id if supplied.
        If the sound is no longer playing, this has no effect.
        :param: the sound id (optional)
        :return:
        """
        pass

    @abstractmethod
    def resume( self, sound_id: int = None ):
        """
        Resumes all paused instances of this sound, or the specified sound id if supplied.
        If the sound is no longer playing, this has no effect.
        :param: the sound id (optional)
        :return:
        """
        pass

    @abstractmethod
    def set_looping( self, sound_id: int, looping: bool ):
        """
        Sets the sound instance with the given id to be looping. If the sound is no
        longer playing this has no effect.
        :param sound_id: the sound id
        :param looping: whether to loop the sound or not
        :return:
        """
        pass

    @abstractmethod
    def set_pitch( self, sound_id: int, pitch: float ):
        """
        Changes the pitch multiplier of the sound instance with the given id as
        returned by :func:`play()` or :func:`play(float)`. If ther sound is no
        longer playing, this has no effect.
        :param sound_id: the sound id
        :param pitch:
        The pitch multiplier, 1 == default, greater than 1 == faster, less than
        1 == slower. Maximum and Minimum are 2.0 and 0.5 respectively.
        :return:
        """
        pass

    @abstractmethod
    def set_volume( self, sound_id: int, volume: float ):
        """
        Changes the volume of the sound instance with the given id as returned by
        :func:`~play()' or :func:'~play(float)'
        :param sound_id: the sound id
        :param volume: the volume, in the range 0 (silent) to 1.0 (max volume)
        :return:
        """
        pass

    @abstractmethod
    def set_pan( self, sound_id: int, pan: float, volume: float ):
        """
        Sets the panning and volume of the sound instance with the given id as returned
        :func:`~play()' or :func:'~play(float)'
        :param sound_id: the sound id
        :param pan: panning in the range -1 (full left) to 1 (full right). 0 is center position.
        :param volume: the volume, in the range 0 (silent) to 1.0 (max volume)
        :return:
        """
        pass
