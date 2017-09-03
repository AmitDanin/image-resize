import cStringIO
from PIL import Image

DEFAULT_RATIO = 0.5


def resize(data, ratio=DEFAULT_RATIO):
    """
    Resize an image
    :param data: The data of the image to resize
    :param ratio: The ratio of the resized image.
    :return: content of the resized image
    """
    imo_handle = cStringIO.StringIO(data)
    img = Image.open(imo_handle)
    try:
        new_size = img.size[0] * ratio, img.size[1] * ratio
        img.thumbnail(new_size, Image.ANTIALIAS)
        return img.tobytes()
    finally:
        img.close()
        imo_handle.close()
