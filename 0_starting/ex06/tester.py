from ft_filter import ft_filter


def myFunc(x):
    """Any function needed to test that both filter()
    and ft_filter() have the same behaviour"""
    if x < 18:
        return False
    else:
        return True


def main():
    ages = [5, 12, 17, 18, 24, 32, -2, 42e42]
    adults = filter(myFunc, ages)
    ft_adults = ft_filter(myFunc, ages)

    if all(x1 == x2 for x1, x2 in zip(adults, ft_adults)):
        print("Okayyy let's go")
    else:
        print("Ay caramba")


if __name__ == "__main__":
    main()
