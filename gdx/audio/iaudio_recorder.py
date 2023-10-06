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


class IAudioRecorder(ABC):

    @abstractmethod
    def read( self, samples, offset, num_samples ):
        """
        Reads in numSamples samples into the array samples starting at
        offset. If the recorder is in stereo you have to multiply
        numSamples by 2.
        :param samples: the array to write the samples to
        :param offset: the offset into the array
        :param num_samples: The number of samples to be read
        """
        pass
