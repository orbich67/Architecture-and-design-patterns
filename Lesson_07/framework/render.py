from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def rendering(templates, folder='templates', **kwargs):
    environ = Environment()
    environ.loader = FileSystemLoader(folder)
    template = environ.get_template(templates)
    return template.render(**kwargs).encode('utf-8')
