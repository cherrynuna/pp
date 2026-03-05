import sys

NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ",
    "3": "...-- ", "4": "....- ", "5": "..... ",
    "6": "-.... ", "7": "--... ", "8": "---.. ",
    "9": "----. ",
    " ": "/ "
}


def main():
    """
    Convert a string argument into Morse code.
    Supports alphanumeric characters and spaces.
    Spaces are represented by '/'.
    Characters are separated by a single space.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")

        text = sys.argv[1].upper()

        # alphanumeric + space 체크
        if not all(c.isalnum() or c == " " for c in text):
            raise AssertionError("AssertionError: the arguments are bad")

        result = ""

        for c in text:
            result += NESTED_MORSE[c]

        print(result.rstrip())

    except AssertionError as ae:
        print(ae)


if __name__ == "__main__":
    main()