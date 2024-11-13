def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns x exposed by himself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns an object with a static-like count,
    i.e. subsequent calls will result and subsequent
    operations on the initial number.
    """
    count = 0

    def inner() -> float:
        nonlocal count
        result = x
        for i in range(count + 1):
            result = function(result)
        count += 1
        return result

    return inner
