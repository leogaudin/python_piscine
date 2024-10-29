def ft_tqdm(lst: range) -> None:  # type: ignore
    """Takes a range. Generates a progress bar depending
    at what step of the range we are currently."""

    try:
        i = 0
        total = len(lst)

        for elem in lst:
            i += 1
            percentage = round(100 * i / total)

            print(
                "{}%|{}| {}/{}".format(
                                    percentage,
                                    '█' * percentage
                                    + ' ' * (100 - percentage),
                                    i,
                                    total
                                ),
                end='\r'
            )
            yield elem

    except BaseException as e:
        print(type(e).__name__, ":", e)
