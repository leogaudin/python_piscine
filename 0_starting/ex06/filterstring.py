import sys


def main():
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
