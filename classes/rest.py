
class RestFullAPI:
    status = 200
    def __init__(self, content_type='application/json'):
        self.content_type = content_type
    
    def rest(self, request):
        if request.method == 'GET':
            return self.get_request()
        elif request.method == 'POST':
            return self.post_request(request)

    def get_type(self):
        return self.content_type

    def get_request(self):
        pass

    def post_request(self, req):
        pass

    