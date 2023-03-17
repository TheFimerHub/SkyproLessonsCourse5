import re

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
              '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}


def decode_bits(bits):
    result = ""
    bits = bits.strip('0')
    minimum = 100000
    count = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i - 1]:
            count += 1
        else:
            if count < minimum:
                minimum = count
            count = 1

    words = bits.split("0"*7*minimum)

    for word in words:
        chars = word.split("0"*3*minimum)
        for chr in chars:
            s = chr.split("0"*minimum)
            for i in s:
                if i == "1" * 3 * minimum:
                    result += "-"
                else:
                    result += "."
            result += " "
        result += "  "

    return result


def decode_morse(morse_code):
    result = ""
    morse_code.strip()
    sym = morse_code.split(" ")
    for i in sym:
        if i != "":
            result += MORSE_CODE[i]
        else:
            result += " "
    return " ".join(result.split())

print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))