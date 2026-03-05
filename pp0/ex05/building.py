import sys
import string


def main():
    """
    Count and display the number of upper letters, lower letters,
    punctuation marks, spaces, and digits in a given text.
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError(
                "AssertionError: more than one argument is provided"
                )

        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = input()
        else:
            text = sys.argv[1]

        print("The text contains", len(text), "characters:")
        print(sum(1 for c in text if c.isupper()), "upper letters")
        print(sum(1 for c in text if c.islower()), "lower letters")
        print(
            sum(1 for c in text if c in string.punctuation),
            "punctuation marks"
            )
        print(sum(1 for c in text if c.isspace()), "spaces")
        print(sum(1 for c in text if c.isdigit()), "digits")

    except EOFError:
        pass
    except AssertionError as ae:
        print(ae)


if __name__ == "__main__":
    main()
