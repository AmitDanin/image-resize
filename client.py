import base64

import tasks


def resize_async(image_path):
    with open(image_path, mode="rb") as f:
        data = f.read()
    return tasks.resize_image.delay(base64.b16decode(data))
