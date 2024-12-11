def ft_filter(
    function,
    iterable,
):
    """Return an iterator yielding those items of iterable for which function\
(item)
    is true. If function is None, return the items that are true."""
    if function is not None:
        return iter([item for item in iterable if function(item)])

    return iter([item for item in iterable if item])
