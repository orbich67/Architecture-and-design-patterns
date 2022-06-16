from views import *

url = {
    '/': index,
    '/category_create/': CategoryCreateView(),
    '/course_create/': create_course,
    '/category_list/': CategoryListView(),
    '/course_list/': course_list,
    '/course_copy/': course_copy,
    '/student_list/': StudentListView(),
    '/student_create/': StudentCreateView(),
    '/student_add/': AddStudentByCourseCreateView(),
}
