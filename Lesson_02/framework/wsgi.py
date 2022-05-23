from framework.request import *
from framework.render import rendering


class AppClass:

    def __init__(self, url: dict):
        self.url = url

    def __call__(self, environ, start_response):
        request = Request(environ)
        path = request.path
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.url:
            view = self.url[path]
            text = view(request)
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [text]
        else:
            start_response('404 PAGE NOT FOUND', [('Content-Type', 'text/html')])
            return [rendering('404.html', 'framework')]
