import sys


def main():
    """Takes a string as first argument and a number as second.
    Prints a list of every string having a larger length than
    the provided number."""

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            int(sys.argv[2])
        except ValueError:
            raise AssertionError("argument is not an integer")

        strings = sys.argv[1].split()
        length = int(sys.argv[2])

        print([(lambda s: s)(s) for s in strings if len(s) > length])

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == "__main__":
    main()
