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
        pass

    @abstractmethod
    def is_playing(self):
        pass

    @abstractmethod
    def set_looping(self, is_looping):
        pass

    @abstractmethod
    def is_looping(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_pan(self, pan, volume):
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
