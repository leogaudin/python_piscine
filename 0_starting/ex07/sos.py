import sys


def main():
    NESTED_MORSE = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        string = sys.argv[1].upper()
        if not all([
            set(NESTED_MORSE.keys()).issuperset(c) for c in string
        ]):
            raise AssertionError("the arguments are bad")

        print(" ".join([NESTED_MORSE[c] for c in string]))

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == "__main__":
    main()
