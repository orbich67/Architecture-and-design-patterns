from framework.render import rendering


def index():
    return rendering('index.html')


def about():
    return rendering('about.html')
