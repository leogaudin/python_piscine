import sys


def get_user_input() -> str:
    """Returns the user input, like the input() function,
    but returns the newline character and handles ^D"""
    try:
        print("What is the text to count?")
        stdin = open(0, "r")
        return stdin.readline()
    except BaseException as e:
        print(type(e).__name__, ":", e)


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 2:
            string = sys.argv[1]
        else:
            string = get_user_input()

        uppercase = len([c for c in string if c.isupper()])
        lowercase = len([c for c in string if c.islower()])
        punctuation = len([
                        c for c in string
                        if set(
                            "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
                        ).issuperset(c)
                    ])
        space = len([c for c in string if c.isspace()])
        digit = len([c for c in string if c.isdigit()])

        print("The text contains", len(string), "characters:")
        print(uppercase, "upper letters")
        print(lowercase, 'lower letters')
        print(punctuation, 'punctuation marks')
        print(space, 'spaces')
        print(digit, 'digits')

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == "__main__":
    main()
