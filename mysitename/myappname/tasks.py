import time
from mysitename.celery import app

@app.task(bind=True)
def async_time_consuming_task(self, time_consumed=5):
    time.sleep(time_consumed)
    print("Slow process completed! ASYNC")