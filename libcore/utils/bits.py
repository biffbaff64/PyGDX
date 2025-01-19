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

class Bits:

    _bits: []

    def __init__(self, nbits: int):
        _bits = [nbits]

    def is_set(self, index: int) -> bool:
        """
        Checks if the bit at the given index is set.
        Args:
            index: The index of the bit to check.
        Returns:
            True if the bit is set, False otherwise.
        """
        word = index >> 6  # Equivalent to >>> in C# for non-negative integers

        if word >= len(self._bits):
            return False

        return (self._bits[word] & (1 << (index & 0x3F))) != 0

    @property
    def is_empty(self) -> bool:
        """
        Checks if all bits are zero.
        Returns:
            True if all bits are zero, False otherwise.
        """
        for t in self._bits:
            if t != 0:
                return False
        return True

    @property
    def all_empty(self) -> bool:
        """
        Checks if all bits are zero using all().
        Returns:
            True if all bits are zero, False otherwise.
        """
        return all(t == 0 for t in self._bits)

    def get_and_clear(self, index: int) -> bool:
        """
        Gets the bit at the given index and clears it.
        Args:
            index: The index of the bit.
        Returns:
            True if the bit was set before invocation, False otherwise.
        """
        word = index >> 6

        if word >= len(self._bits):
            return False

        old_bits = self._bits[word]

        self._bits[word] &= ~(1 << (index & 0x3F))

        return self._bits[word] != old_bits

    def get_and_set(self, index: int) -> bool:
        """
        Gets the bit at the given index and sets it.
        Args:
            index: The index of the bit.
        Returns:
            True if the bit was already set, False otherwise.
        """
        word = index >> 6

        self.ensure_capacity(word)  # Call ensure_capacity

        old_bits = self._bits[word]

        self._bits[word] |= 1 << (index & 0x3F)

        return self._bits[word] == old_bits

    def ensure_capacity(self, word: int):
        """
        Ensures that the _bits list has enough capacity.
        Args:
            word: The index of the word to check capacity for.
        """
        if word >= len(self._bits):
            self._bits.extend([0] * (word - len(self._bits) + 1))  # Extend the list to the required size

    def set_bit(self, index: int):
        """
        Sets the bit at the given index.
        Args:
            index: The index of the bit to set.
        """
        word = index >> 6
        self.ensure_capacity(word)
        self._bits[word] |= 1 << (index & 0x3F)

    def flip_bit(self, index: int):
        """
        Flips the bit at the given index.
        Args:
            index: The index of the bit to flip.
        """
        word = index >> 6
        self.ensure_capacity(word)
        self._bits[word] ^= 1 << (index & 0x3F)

    def clear_bit(self, index: int):
        """
        Clears the bit at the given index.
        Args:
            index: The index of the bit to clear.
        """
        word = index >> 6

        if word >= len(self._bits):
            return

        self._bits[word] &= ~(1 << (index & 0x3F))

    def clear_all(self):
        """
        Clears all bits in the bitset.
        """
        self._bits = [0] * len(self._bits)  # Most efficient and clear way in python

    def num_bits(self) -> int:
        """
        Returns the total number of bits the BitSet can hold.
        Returns:
            The total number of bits.
        """
        return len(self._bits) << 6

    def length(self) -> int:
        """
        Returns the logical size of the bitset.
        Returns:
            The logical size (index of the highest set bit + 1), or 0 if empty.
        """
        for word in range(len(self._bits) - 1, -1, -1):
            bits_at_word = self._bits[word]
            if bits_at_word != 0:
                for bit in range(63, -1, -1):
                    if (bits_at_word & (1 << bit)) != 0:
                        return (word << 6) + bit + 1
        return 0

    def next_set_bit(self, from_index: int) -> int:
        """
        Returns the index of the next set bit on or after from_index.
        Args:
            from_index: The starting index.
        Returns:
            The index of the next set bit, or -1 if none exists.
        """
        word = from_index >> 6

        if word >= len(self._bits):
            return -1

        bits_at_word = self._bits[word]

        if bits_at_word != 0:
            for i in range(from_index & 0x3f, 64):
                if (bits_at_word & (1 << i)) != 0:
                    return (word << 6) + i

        for word in range(word + 1, len(self._bits)):
            bits_at_word = self._bits[word]
            if bits_at_word != 0:
                for i in range(64):
                    if (bits_at_word & (1 << i)) != 0:
                        return (word << 6) + i

        return -1

    def next_clear_bit(self, from_index: int) -> int:
        """
        Returns the index of the next clear bit on or after from_index.
        Args:
            from_index: The starting index.
        Returns:
            The index of the next clear bit, or the length of the bitset if none exists.
        """
        word = from_index >> 6

        if word >= len(self._bits):
            return len(self._bits) << 6

        bits_at_word = self._bits[word]

        for i in range(from_index & 0x3f, 64):
            if (bits_at_word & (1 << i)) == 0:
                return (word << 6) + i

        for word in range(word + 1, len(self._bits)):
            bits_at_word = self._bits[word]
            for i in range(64):
                if (bits_at_word & (1 << i)) == 0:
                    return (word << 6) + i

        return len(self._bits) << 6

    def and_bits(self, other):
        """
        Performs a bitwise AND operation with another BitSet.
        Args:
            other: The other BitSet.
        """
        common_words = min(len(self._bits), len(other.get_bits()))

        for i in range(common_words):
            self._bits[i] &= other.get_bits()[i]

        if len(self._bits) > common_words:
            self._bits[common_words:] = [0] * (len(self._bits) - common_words)  # Slicing is more efficient than a loop

    def and_not(self, other):
        """
        Performs a bitwise AND NOT operation with another BitSet.
        Args:
            other: The other BitSet.
        """
        for i in range(min(len(self._bits), len(other.get_bits()))):
            self._bits[i] &= ~other.get_bits()[i]

    def or_bits(self, other):
        """
        Performs a bitwise OR operation with another BitSet.
        Args:
            other: The other BitSet.
        """
        common_words = min(len(self._bits), len(other.get_bits()))

        for i in range(common_words):
            self._bits[i] |= other.get_bits()[i]

        if common_words < len(other.get_bits()):
            self.ensure_capacity(len(other.get_bits()))
            self._bits[common_words:] = other.get_bits()[common_words:]  # Efficient copy using slicing

    def xor_bits(self, other):
        """
        Performs a bitwise XOR operation with another BitSet.
        Args:
            other: The other BitSet.
        """
        common_words = min(len(self._bits), len(other.get_bits()))

        for i in range(common_words):
            self._bits[i] ^= other.get_bits()[i]

        if common_words < len(other.get_bits()):
            self.ensure_capacity(len(other.get_bits()))
            self._bits[common_words:] = other.get_bits()[common_words:]  # Efficient copy using slicing

    def intersects(self, other) -> bool:
        """
        Checks if this BitSet intersects with another BitSet.
        Args:
            other: The other BitSet.
        Returns:
            True if the BitSets intersect, False otherwise.
        """
        for i in range(min(len(self._bits), len(other.get_bits())) - 1, -1, -1):
            if (self._bits[i] & other.get_bits()[i]) != 0:
                return True
        return False

    def contains_all(self, other) -> bool:
        """
        Checks if this BitSet contains all bits of another BitSet.
        Args:
            other: The other BitSet.
        Returns:
            True if this BitSet contains all bits of the other, False otherwise.
        """
        bits_len = len(self._bits)
        other_bits_len = len(other.get_bits())

        for i in range(bits_len, other_bits_len):
            if other.get_bits()[i] != 0:
                return False

        for i in range(min(bits_len, other_bits_len) - 1, -1, -1):
            if (self._bits[i] & other.get_bits()[i]) != other.get_bits()[i]:
                return False

        return True

    def __eq__(self, other):
        """
        Checks if this BitSet is equal to another object.
        Args:
            other: The object to compare with.
        Returns:
            True if the objects are equal, False otherwise.
        """
        if self is other:
            return True

        if other is None:
            return False

        if type(self) is not type(other):
            return False

        common_words = min(len(self._bits), len(other.get_bits()))

        for i in range(common_words):
            if self._bits[i] != other.get_bits()[i]:
                return False

        if len(self._bits) == len(other.get_bits()):
            return True

        return self.length() == other.length()

    def get_bits(self) -> []:
        """
        Gets the '_bits' list
        """
        return self._bits

    def get_bit(self, index: int) -> int:
        """
        Gets the element from the '_bits' list at the specified index
        :param index:
        :return:
        """
        return self._bits[index]
