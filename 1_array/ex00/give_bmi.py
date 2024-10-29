import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Takes a list of heights and a list of weights.
    Returns a list of BMIs."""

    try:
        np_height = np.array(height)
        np_weight = np.array(weight)

        np_bmi = np_weight / (np_height ** 2)

        return np_bmi.tolist()

    except BaseException as e:
        print(type(e).__name__, ":", e)


def apply_limit(
    bmi: list[int | float],
    limit: int
) -> list[bool]:
    """Takes a list of BMIs and a limit as parameters.
    Returns a list of booleans."""

    try:
        map_limit = np.vectorize(lambda bmi: bmi > limit)

        return np.array(map_limit(bmi)).tolist()

    except BaseException as e:
        print(type(e).__name__, ":", e)
