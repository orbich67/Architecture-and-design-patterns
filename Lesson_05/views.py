import datetime
from framework.render import rendering
from model import TrainingSite
from logs import Logger, debug

site = TrainingSite()
logger1 = Logger('view')
logger2 = Logger('create')
logger3 = Logger('visit')


def index(request):
    time = datetime.datetime.now()
    logger3.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} посещение страницы "index.html"')
    return rendering('index.html', objects_list=site.courses, title='Главная страница')


@debug
def create_category(request):
    if request.method == 'POST':
        time = datetime.datetime.now()
        data = request.body
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
        logger2.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} создана категория с именем: {name}')
        new_category = site.create_category(name, category)

        site.categories.append(new_category)
        return rendering('category_create.html', title='Создание категории')

    else:
        categories = site.categories
        return rendering('category_create.html', categories=categories, title='Создание категории')


@debug
def create_course(request):
    if request.method == 'POST':
        time = datetime.datetime.now()
        data = request.body
        name = data['name']
        category_id = data.get('category_id')
        if name and category_id:
            category = site.find_category_by_id(int(category_id))
            course = site.create_course('record', name, category)
            site.courses.append(course)
            logger2.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} создан курс с именем: {name}')
        return rendering('course_create.html', title='Создание курса')
    else:
        categories = site.categories
        return rendering('course_create.html', categories=categories, title='Создание курса')


def course_list(request):
    time = datetime.datetime.now()
    logger1.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} просмотр списка курсов.')
    return rendering('course_list.html', objects_list=site.courses, title='Список курсов')


def course_copy(request):
    query_params = request.query_params
    name = query_params['name']
    old_course = site.get_course(name)
    if old_course:
        new_name = f'{name}_copy'
        new_course = old_course.clone()
        new_course.name = new_name
        site.courses.append(new_course)
    return rendering('course_list.html', objects_list=site.courses, title='Список курсов')


def category_list(request):
    time = datetime.datetime.now()
    logger1.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} просмотр списка категорий.')
    return rendering('category_list.html', objects_list=site.categories, title='Список категорий')
