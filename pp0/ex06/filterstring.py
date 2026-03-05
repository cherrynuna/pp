import sys
from ft_filter import ft_filter


def main():
    """
    Program that prints words from a string whose length is greater than N.
    Command line usage:
        python filterstring.py "<String>" <N>
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        S = sys.argv[1]

        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")

        # lambda + list comprehension 사용
        result = list(
            ft_filter(
                lambda w: len(w) > N,
                [w for w in S.split(" ")]
            )
        )

        print(result)

    except AssertionError as ae:
        print(ae)


if __name__ == "__main__":
    main()
