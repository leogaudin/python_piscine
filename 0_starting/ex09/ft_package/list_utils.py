def count_in_list(lst: list[str], string: str) -> int:
    """Takes a list of strings as first parameter and a string
    as second.
    Returns the number of occurences of the given string in the
    list."""

    try:
        if lst is None or string is None:
            raise AssertionError("arguments are bad")

        return sum([1 for s in lst if s == string])

    except BaseException as e:
        print(type(e).__name__, ":", e)
