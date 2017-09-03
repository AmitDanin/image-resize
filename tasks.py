import base64
from celery import Celery
import image

MQ_URL = 'amqp://tvibxhwo:wFf6GRnN-rRIt4nIT0geHlMYImOamUqW@orangutan.rmq.cloudamqp.com/tvibxhwo'

app = Celery('tasks', broker=MQ_URL, backend=MQ_URL)


@app.task
def resize_image(data, resize_ratio=image.DEFAULT_RATIO):
    return base64.encode(image.resize(base64.b64decode(data)))
