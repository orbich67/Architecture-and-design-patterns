from framework.wsgi import AppClass
from url import url

# запуск: gunicorn main:app
# параметры по умолчанию - localhost:8000
app = AppClass(url)
