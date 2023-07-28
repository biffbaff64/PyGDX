from abc import ABC, abstractmethod


class IAudioRecorder(ABC):

    @abstractmethod
    def read( self, samples, offset, num_samples ):
        pass

    @abstractmethod
    def dispose( self ):
        pass
