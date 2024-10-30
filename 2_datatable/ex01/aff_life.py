from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Loads the life expectancy dataset, transposes it and plot
    only the data for Spain.
    """
    try:
        df = load("./2_datatable/life_expectancy_years.csv")
        df = df.T
        country = 'Portugal'
        data = df[country]
        data.plot(
            xlabel='Year',
            ylabel='Life expectancy',
            title=(country + ' life expectancy projections')
        )
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
