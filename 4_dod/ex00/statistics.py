def ft_mean(args: list[int | float]):
    """Returns the mean of the provided list."""
    return sum(args) / len(args)


def ft_median(args: list[int | float]):
    """Returns the median of the provided list."""
    numbers = list(args)
    numbers.sort()
    length = len(numbers)

    if length % 2 == 0:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        return numbers[(length + 1) // 2 - 1]


def ft_quartile(args: list[int | float]):
    """Returns the first and third quartiles of the provided list."""
    numbers = list(args)
    numbers.sort()
    median = ft_median(numbers)

    first = ft_median(filter(lambda x: x <= median, numbers))
    third = ft_median(filter(lambda x: x >= median, numbers))

    return [first, third]


def ft_std(args: list[int | float]):
    """Returns the standard deviation of the provided list."""
    mean = ft_mean(args)
    partial_sum = [(x - mean) ** 2 for x in args]
    return (sum(partial_sum) / len(args)) ** .5


def ft_var(args: list[int | float]):
    """Returns the variance of the provided list."""
    mean = ft_mean(args)
    partial_sum = [(x - mean) ** 2 for x in args]
    return sum(partial_sum) / len(args)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Takes a list of numbers through args, and does the
    operations specified in kwargs.
    """
    operations = {
        'mean': ft_mean,
        'median': ft_median,
        'quartile': ft_quartile,
        'std': ft_std,
        'var': ft_var,
    }

    try:
        if not all(isinstance(arg, int | float) for arg in args):
            raise ValueError('One or more NaN arguments')

        for _, value in kwargs.items():
            if value in operations.keys():
                if len(args) > 0:
                    print(value, ':', operations[value](args))
                else:
                    print('ERROR')

    except BaseException as e:
        print(type(e).__name__, ':', e)
