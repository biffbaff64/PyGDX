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
import struct

from gdx.core import iinput_processor


class InputEventQueue:

    Skip: int = -1
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

        # Assuming q is a list representing the processing queue
        for i in range(0, len(self._processing_queue), 3):
            event_type = self._processing_queue[i]
            _current_event_time = (self._processing_queue[i + 1] << 32) | (self._processing_queue[i + 2] & 0xFFFFFFFF)

            if event_type == self.Skip:
                i += self._processing_queue[i]

            elif event_type == self.Key_Down:
                processor.key_down(self._processing_queue[i + 1])

            elif event_type == self.Key_Up:
                processor.key_up(self._processing_queue[i + 1])

            elif event_type == self.Key_Typed:
                processor.key_typed(chr(self._processing_queue[i + 1]))

            elif event_type == self.Touch_Down:
                processor.touch_down(self._processing_queue[i + 1], self._processing_queue[i + 2],
                                     self._processing_queue[i + 3], self._processing_queue[i + 4])

            elif event_type == self.Touch_Up:
                processor.touch_up(self._processing_queue[i + 1], self._processing_queue[i + 2],
                                   self._processing_queue[i + 3], self._processing_queue[i + 4])

            elif event_type == self.Touch_Dragged:
                processor.touch_dragged(self._processing_queue[i + 1], self._processing_queue[i + 2],
                                        self._processing_queue[i + 3])

            elif event_type == self.Mouse_Moved:
                processor.mouse_moved(self._processing_queue[i + 1], self._processing_queue[i + 2])

            elif event_type == self.Mouse_Scrolled:
                processor.scrolled(
                    struct.unpack('f', struct.pack('I', self._processing_queue[i + 1]))[0],
                    struct.unpack('f', struct.pack('I', self._processing_queue[i + 2]))[0]
                    )

            else:
                raise Exception("Invalid event type")

    def next(self, next_type: int, i: int) -> int:

        for n in range(0, len(self._processing_queue), 3):
            type = self._processing_queue[i]

            if type == next_type:
                return i


        pass
