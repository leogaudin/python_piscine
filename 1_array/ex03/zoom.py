from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def main():
    try:
        rgb = ft_load('./1_array/ex03/animal.jpeg')
        zoomed = rgb[200:600, 500:900]

        # We can do the mean for every pixel, but it's honestly
        # close enough with just keeping the R channel.
        #
        # for y in range(len(sliced_rgb)):
        #     for x in range(len(sliced_rgb[y])):
        #         sliced_rgb[y][x] = np.mean(sliced_rgb[y][x])

        grayed = zoomed[:, :, 0:1].reshape(400, 400)
        print('New shape after slicing:', grayed.shape)
        print(grayed)

        image = Image.fromarray(grayed)
        plt.imshow(image, 'gray')
        plt.show()

    except BaseException as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
