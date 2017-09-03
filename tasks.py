import base64
from celery import Celery
import image

app = Celery('tasks',
             broker='amqp://tvibxhwo:wFf6GRnN-rRIt4nIT0geHlMYImOamUqW@orangutan.rmq.cloudamqp.com/tvibxhwo',
             backend='rpc://')


@app.task
def resize_image(data, resize_ratio=image.DEFAULT_RATIO):
    image.resize(base64.b64decode(data))
