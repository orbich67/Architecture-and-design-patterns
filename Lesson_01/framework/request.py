class Request:

    def __init__(self, environ):
        self.headers = self._get_http_headers(environ)
        self.method = environ.get('REQUEST_METHOD')
        self.body = environ.get('wsgi.input')
        self.query_params = self._get_query_params(environ)
        # в ubuntu environ 'path' - 'RAW_URI'
        self.path = environ.get('RAW_URI')


    def _get_http_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            # print(key, value)
            if key.startswith('HTTP_'):
                headers[key[5:]] = value
        return headers

    def _get_query_params(self, environ):
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
