import os
import time
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zapis.settings')

app = Celery('zapis')
app.config_from_object('django.conf:settings')

# Устанавливаем broker_url
app.conf.broker_url = settings.CELERY_BROKER_URL

# Автоматически обнаруживаем задачи
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print('Hello from debug_task')

# docker-compose run --rm web-app sh -c "python manage.py shell"
# from celery_app import debug_task