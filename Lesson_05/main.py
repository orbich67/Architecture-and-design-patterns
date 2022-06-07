import datetime
from framework.wsgi import *
from url import url
from framework.render import rendering
from views import logger3

# запуск: gunicorn main:app
# параметры по умолчанию - localhost:8000
# app = AppClass(url, front_controllers)
front_controllers = []

# app = AppClass(url, front_controllers)
app = LogApplication(url, front_controllers)
# app = FakeApplication(url, front_controllers)


@app.route('/about/')
def about(request):
    time = datetime.datetime.now()
    logger3.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} посещение страницы "about.html"')
    return rendering('about.html', title='О нас')
