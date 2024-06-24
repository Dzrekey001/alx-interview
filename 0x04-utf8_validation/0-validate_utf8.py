#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    a method that determines if a given data set represents a valid UTF-8
    encoding.
    """
    number_of_byte = 0

    for char in data:
        byte = char & 0xFF

        if number_of_byte == 0:
            if (byte >> 5) == 0b110:
                number_of_byte = 1
            elif (byte >> 4) == 0b1110:
                number_of_byte = 2
            elif (byte >> 3) == 0b11110:
                number_of_byte = 3
            elif (byte >> 7) == 0:
                pass
            else:
                return False
        else:
            if (byte >> 6) == 0b10:
                number_of_byte -= 1
            else:
                return False
    return number_of_byte == 0
