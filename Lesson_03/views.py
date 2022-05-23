import datetime
from framework.render import rendering
from staff import *


def index(request):
    return rendering('index.html')


def about(request):
    return rendering('about.html')


def contacts(request):
    if request.method == 'POST':
        data = request.body
        recv_time = datetime.datetime.now()
        title, text, email = data['title'], data['text'], data['email']
        if title and text and email:
            with open(f'message_from_site.txt', 'a',
                      encoding='utf-8') as file:
                file.write(f'{recv_time.strftime("%d.%m.%Y")} в {recv_time.strftime("%H:%M:%S")} получено сообщение:\n'
                           f'Тема: {title}\n'
                           f'Текст: {text}\n'
                           f'Отправитель: {email}\n'
                           f'-----\n')
    return rendering('contacts.html')


def view_all_contacts(request):
    return rendering('staff.html', staff=request.controller)


def supervisor(request):
    return rendering('staff.html', staff=request.controller[0:1])


def sales(request):
    return rendering('staff.html', staff=request.controller[1:4])
