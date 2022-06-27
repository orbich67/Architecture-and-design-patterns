import datetime
from framework.render import rendering
from framework.cbv import CreateView, ListView
from framework.unitwork import UnitOfWork
from model import TrainingSite, MapperRegistry
from logs import Logger, debug
from urllib.parse import unquote

site = TrainingSite()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)

logger1 = Logger('view')
logger2 = Logger('create')
logger3 = Logger('visit')


def index(request):
    time = datetime.datetime.now()
    logger3.log(f'{time.strftime("%d.%m.%Y")} в {time.strftime("%H:%M:%S")} посещение страницы "index.html"')
    return rendering('index.html', objects_list=site.courses, title='Главная страница')


# ----- Class-based views (CBV) -----
class CategoryCreateView(CreateView):
    template_name = 'category_create.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = unquote(data['name'])
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)


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


# Class-based views (CBV)
class CategoryListView(ListView):
    queryset = site.categories
    template_name = 'category_list.html'


class StudentListView(ListView):

    def get_queryset(self):
        mapper = MapperRegistry.get_current_mapper('student')
        return mapper.all()
    template_name = 'student_list.html'
    queryset = get_queryset


class StudentCreateView(CreateView):
    template_name = 'student_create.html'

    def create_obj(self, data: dict):
        name = unquote(data['name'])
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)
        new_obj.mark_new()
        UnitOfWork.get_current().commit()


class AddStudentByCourseCreateView(CreateView):
    template_name = 'student_add.html'


    def get_queryset(self):
        mapper = MapperRegistry.get_current_mapper('student')
        return mapper.all()

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = self.get_queryset()
        return context

    def create_obj(self, data: dict):
        course_name = unquote(data['course_name'])
        course = site.get_course(course_name)
        student_name = unquote(data['student_name'])
        student = site.get_student(student_name)
        course.add_student(student)
