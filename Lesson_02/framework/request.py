import re


class Request:

    def __init__(self, environ):
        self.headers = self._get_http_headers(environ)
        self.method = environ.get('REQUEST_METHOD')
        self.body = self._get_query_body(environ)
        self.query_params = self._get_query_params(environ)
        self.path = environ.get('PATH_INFO')

    @staticmethod
    def _get_http_headers(environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:]] = value
        return headers

    @staticmethod
    def _get_query_params(environ):
        query_params = {}
        data = environ['QUERY_STRING'].split('&')
        for el in data:
            if el:
                key, value = el.split('=')
                if query_params.get(key):
                    query_params[key].append(value)
                else:
                    query_params[key] = value
        return query_params

    @staticmethod
    def _get_query_body(environ):
        pattern = '%40'
        data = environ['wsgi.input'].read()
        if data:
            data = data.decode(encoding='utf-8')
            result_dict = {}
            data = re.sub(pattern, '@', data)
            data = data.split('&')
            for el in data:
                key, value = el.split('=')
                result_dict[key] = value.replace('+', ' ')
            return result_dict
        return None
