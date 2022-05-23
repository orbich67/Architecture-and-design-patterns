from jinja2 import Environment, FileSystemLoader


def rendering(templates, folder='templates', **kwargs):
    environ = Environment()
    environ.loader = FileSystemLoader(folder)
    template = environ.get_template(templates)
    return template.render(**kwargs).encode('utf-8')
