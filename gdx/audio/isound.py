from abc import ABC, abstractmethod


class ISound(ABC):

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

    def stop( self, sound_id: int ):
        """
        Stops playing all instances of this sound, or the specified sound id if supplied.
        If the sound is no longer playing, this has no effect.
        :param: the sound id (optional)
        :return:
        """
        pass

    def pause( self, sound_id: int ):
        """
        Pauses all instances of this sound, or the specified sound id if supplied.
        If the sound is no longer playing, this has no effect.
        :param: the sound id (optional)
        :return:
        """
        pass

    def resume( self, sound_id: int ):
        """
        Resumes all paused instances of this sound, or the specified sound id if supplied.
        If the sound is no longer playing, this has no effect.
        :param: the sound id (optional)
        :return:
        """
        pass


    /// <summary>
    /// Sets the sound instance with the given id to be looping. If the sound is no longer
    /// playing this has no effect.
    /// </summary>
    /// <param name="soundId"> the sound id </param>
    /// <param name="looping"> whether to loop or not.  </param>
    void SetLooping( long soundId, bool looping );

    /// <summary>
    /// Changes the pitch multiplier of the sound instance with the given id as returned
    /// by <see cref="play()"/> or <see cref="play(float)"/>.
    /// If the sound is no longer playing, this has no effect.
    /// </summary>
    /// <param name="soundId"> the sound id </param>
    /// <param name="pitch">
    /// the pitch multiplier, 1 == default, greater than 1 == faster, less than 1 == slower,
    /// the value has to be between 0.5 and 2.0
    /// </param>
    void SetPitch( long soundId, float pitch );

    /// <summary>
    /// Changes the volume of the sound instance with the given id as returned by
    /// <see cref="Play()"/> or <see cref="Play(float)"/>. If the
    /// sound is no longer playing, this has no effect.
    /// </summary>
    /// <param name="soundId"> the sound id </param>
    /// <param name="volume"> the volume in the range 0 (silent) to 1 (max volume).  </param>
    void SetVolume( long soundId, float volume );

    /// <summary>
    /// Sets the panning and volume of the sound instance with the given id as returned
    /// by <see cref="Play()"/> or <see cref="Play(float)"/>.
    /// If the sound is no longer playing, this has no effect. Note that panning only works
    /// for mono sounds, not for stereo sounds!
    /// </summary>
    /// <param name="soundId"> the sound id </param>
    /// <param name="pan"> panning in the range -1 (full left) to 1 (full right). 0 is center position. </param>
    /// <param name="volume"> the volume in the range [0,1].  </param>
    void SetPan( long soundId, float pan, float volume );
