from load_csv import load
import matplotlib.pyplot as plt


def remove_human_readable(value: str) -> float:
    """Given a human-readable number string (e.g. 30M, 20K),
    returns the actual number.
    """
    if type(value) is float:
        return value

    try:
        numeric_size = float(value[:-1])
        unit = value[-1]
    except ValueError:
        raise ValueError('Can\'t convert %r to actual' % value)

    unit = unit.upper()

    if unit == 'M':
        actual = numeric_size * 1000000
    elif unit == 'K':
        actual = numeric_size * 1000
    else:
        actual = numeric_size

    return actual


def main():
    """Loads the population dataset, transposes it and plot
    only the data for Spain and Portugal
    """
    try:
        df = load('./2_datatable/population_total.csv')
        df = df.T

        country = 'Spain'
        other_country = 'France'

        data = df[[country, other_country]]
        data = data.map(remove_human_readable)
        first_250 = data.head(250)
        first_250.plot(
            xlabel='Year',
            ylabel='Population',
            title=('Population projections'),
        )
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
