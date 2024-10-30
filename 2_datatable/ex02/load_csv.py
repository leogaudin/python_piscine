import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads the CSV at the specified path, with 'country'
    as index column.
    Returns the data as DataFrame"""

    try:
        df = pd.read_csv(path, index_col='country')
        print('Loading dataset of dimensions', df.shape)
        return df

    except BaseException as e:
        print(type(e).__name__, ":", e)
