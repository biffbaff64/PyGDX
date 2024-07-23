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


class IAudioDevice( ABC ):

    @abstractmethod
    def is_mono( self ) -> bool:
        """
        Returns whether this AudioDevice is in mono or stereo mode.
        """
        pass

    @abstractmethod
    def write_samples( self, samples, offset, num_samples ):
        """
        Writes the array of PCM samples to the audio device and
        blocks until they have been processed.
        :param samples: An int, or float, array of PCM samples
        :param offset: The start index into the array.
        :param num_samples: The number of samples to write
        """
        pass

    @abstractmethod
    def get_latency( self ) -> int:
        pass

    @abstractmethod
    def set_volume( self, vol: float ):
        """
        Sets the volume.
        :param vol: a float holding a valume in the range 0.0 to 1.0
        """
        pass

    @abstractmethod
    def dispose( self ):
        """
        Frees all resources associated with this AudioDevice.
        Needs to be called when the device is no longer needed.
        """
        pass
