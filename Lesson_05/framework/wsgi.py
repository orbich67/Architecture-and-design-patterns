from framework.render import rendering
from framework.request import *


class AppClass:

    def __init__(self, url: dict, front_controllers: list):
        self.url = url
        self.front_controllers = front_controllers

    def route(self, route):
        def inner(view):
            self.url[route] = view
        return inner

    def __call__(self, environ, start_response):
        request = Request(environ)
        request.controller = self.front_controllers
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


class LogApplication(AppClass):

    def __init__(self, url, front_controllers):
        super().__init__(url, front_controllers)

    def __call__(self, environ, start_response):
        request = Request(environ)
        request.controller = self.front_controllers
        path = request.path
        print(f'Тип запроса: {request.method}, параметры: {request.query_params}')
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


class FakeApplication(AppClass):

    def __init__(self, url, front_controllers):
        super().__init__(url, front_controllers)

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake!']
