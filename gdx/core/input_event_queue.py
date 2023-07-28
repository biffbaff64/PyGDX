from gdx.core import iinput_processor


class InputEventQueue:

    Key: int = 1
    Key_Down: int = 0
    Key_Up: int = 1
    Key_Typed: int = 2
    Touch_Down: int = 3
    Touch_Up: int = 4
    Touch_Dragged: int = 5
    Mouse_Moved: int = 6
    Mouse_Scrolled: int = 7

    _queue: list
    _processing_queue: list
    _current_event_time: int

    def drain(self, processor: iinput_processor):
        if processor is None:
            self._queue.clear()
            return

        self._processing_queue.append(processor)
        self._queue.clear()

        q = list_to_array(self._processing_queue)

        for x in self._processing_queue:
