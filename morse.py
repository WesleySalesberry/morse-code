#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
import re

__author__ = 'wesley salesberry'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits = bits.strip('0')
    bits_timing = min([len(element)
                       for element in bits.split('1') + bits.split('0') if element])
    bits_new = bits.replace("0000000" * bits_timing, "   ").replace('111' * bits_timing, '-').replace(
        '1' * bits_timing, '.').replace('000' * bits_timing, " ").replace('0' * bits_timing, '')
    return bits_new
# radio_name = ".-- / -... / ....- / .--. / ... / -.-."
# challenge = "- .... .. ... / .. ... / .- / ... .. -- .--. .-.. . --..-- / -.-- . - / -.-. .... .- .-.. .-.. . -. --. .. -. --. / -.-. .- -.-. .... . .-.-.-"


# def decode_morse(morse):
#     morse_list = morse.split('   ')
#     letters = []
#     for element in morse_list:
#         chars = element.split(' ')
#         for char in chars:
#             for key, value in MORSE_2_ASCII.items():
#                 if char == key:
#                     letters.append(value)
#         letters.append(' ')
#     print(''.join(letters))
#     return ''.join(letters)

def decode_morse(morse):
    morse_list = re.split(r'(\S+)', morse.strip())
    results = ''
    for element in morse_list:
        if MORSE_2_ASCII.get(element):
            results += MORSE_2_ASCII.get(element)
        else:
            results += " "
    print(results)
    return results


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
