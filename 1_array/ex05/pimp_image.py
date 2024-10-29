from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def show_array_as_image(array: npt.NDArray):
    """Shows the provided array as an image."""
    image = Image.fromarray(array)
    plt.imshow(image)
    plt.show()


def ft_invert(array: npt.NDArray) -> npt.NDArray:
    """Inverts the color of the image received."""
    try:
        result = 255 - array
        show_array_as_image(result)
        return result

    except BaseException as e:
        print(type(e).__name__, ":", e)


def ft_red(array: npt.NDArray) -> npt.NDArray:
    """Removes all channels except the R."""

    try:
        height = len(array)
        width = len(array[0])
        result = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                result[y][x] = (0, 0, 0)
                result[y][x][0] = array[y][x][0]

        show_array_as_image(result)
        return result
    except BaseException as e:
        print(type(e).__name__, ":", e)


def ft_green(array: npt.NDArray) -> npt.NDArray:
    """Removes all channels except the G."""
    try:
        height = len(array)
        width = len(array[0])
        result = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                result[y][x] = (0, 0, 0)
                result[y][x][1] = array[y][x][1]

        show_array_as_image(result)
        return result
    except BaseException as e:
        print(type(e).__name__, ":", e)


def ft_blue(array: npt.NDArray) -> npt.NDArray:
    """Removes all channels except the B."""

    try:
        height = len(array)
        width = len(array[0])
        result = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                result[y][x] = (0, 0, 0)
                result[y][x][2] = array[y][x][2]

        show_array_as_image(result)
        return result
    except BaseException as e:
        print(type(e).__name__, ":", e)


def ft_grey(array: npt.NDArray) -> npt.NDArray:
    """Grayscales the image received."""

    try:
        height = len(array)
        width = len(array[0])
        result = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                result[y][x] = array[y][x][1:2]

        show_array_as_image(result)
        return result
    except BaseException as e:
        print(type(e).__name__, ":", e)
