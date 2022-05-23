from framework.wsgi import AppClass
from url import url
from staff import staff


# запуск: gunicorn main:app
# параметры по умолчанию - localhost:8000
app = AppClass(url, staff)
