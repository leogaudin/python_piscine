import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes as parameters a 2D array, prints its shape.
    Returns a truncated version of the array based on the
    provided start and end arguments."""

    try:
        np_family = np.array(family)
        np_sliced_family = np.array(family)[start:end]

        print('My shape is :', np_family.shape)
        print('My new shape is :', np_sliced_family.shape)

        return np_sliced_family.tolist()

    except BaseException as e:
        print(type(e).__name__, ":", e)
