from PIL import Image
import numpy as np
import numpy.typing as npt


def ft_load(path: str) -> npt.NDArray[np.uint8]:
    """Loads an image from a path and returns a 3D array."""
    try:
        image = Image.open(path)
        image.load()
        rgb = np.array(image, dtype=np.uint8)
        print('The shape of image is :', rgb.shape)
        return rgb

    except BaseException as e:
        print(type(e).__name__, ":", e)
