from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        rgb = ft_load('./1_array/animal.jpeg')
        zoomed = rgb[200:600, 500:900]
        grayed = zoomed[:, :, 0:1].reshape(400, 400)
        print('New shape after slicing:', grayed.shape)
        print(grayed)

        transposed = np.zeros(
            shape=(len(grayed), len(grayed[0])),
            dtype=np.uint8
        )

        for y in range(len(grayed)):
            for x in range(len(grayed[y])):
                transposed[y][x] = grayed[x][y]

        image = Image.fromarray(transposed)
        plt.imshow(image, 'gray')
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
