import os
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_celery_app():
    app = Celery('my_app', broker=f'pyamqp://{os.environ["RABBITMQ_DEFAULT_USER"]}@{os.environ["HOSTNAME"]}//')
    app.conf.include = ['worker.tasks']
    app.conf.beat_schedule = {
        'run-every-5-minutes': {
            'task': 'worker.tasks.fetch_data_and_check_rules',
            'schedule': crontab(minute='*/5'),
        },
    }
    return app

app = create_celery_app()
