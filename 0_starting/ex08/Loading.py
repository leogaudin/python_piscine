def ft_tqdm(lst: range) -> None:  # type: ignore
    i = 0
    total = len(lst)

    for elem in lst:
        i += 1
        percentage = round(100 * i / total)

        print(
            "{}%|{}| {}/{}".format(
                                percentage,
                                '█' * percentage + ' ' * (100 - percentage),
                                i,
                                total
                            ),
            end='\r'
        )
        yield elem
