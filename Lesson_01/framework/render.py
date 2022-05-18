from jinja2 import Template
import os


def rendering(templates, folder='templates'):

    file_path = os.path.join(folder, templates)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render().encode('utf-8')
