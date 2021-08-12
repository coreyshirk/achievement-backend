class CORSMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS, DELETE'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Max-Age'] = '1000'
        response['Access-Control-Allow-Headers'] = \
            'X-Request-With, Content-Type, Authorization, X-Request-Group-UUID'
        return response
