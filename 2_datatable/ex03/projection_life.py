from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Loads the life expectancy and GDP datasets, and plots
    the data cloud to highlight a possible correlation.
    """
    try:
        df_life = load('./2_datatable/life_expectancy_years.csv')
        df_gdp = load(
            './2_datatable/income_per_person_gdppercapita'
            + '_ppp_inflation_adjusted.csv'
        )

        df = pd.merge(df_gdp['1900'], df_life['1900'], on='country')
        fig, ax = plt.subplots()
        ax.plot(df['1900_x'], df['1900_y'], 'o')
        ax.set_xscale('log')
        ax.set_xlabel('Gross domestic product')
        ax.set_ylabel('Life expectancy')
        ax.set_title('1900')
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
