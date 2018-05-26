from django.utils import timezone
from users.models import Users
from users.classes.helper import PermanentObj
import json

class GetUser(PermanentObj):
    def __init__(self):
        super(GetUser, self).__init__()

    def post_request(self, req):
        req_body = json.loads(req.body)
        try:
            temp_obj = Users.objects.get(user_login = req_body['login'])
        except:
            self.status = 403
            return 'Authorization user'
        send = 'Authorization error'
        if temp_obj.id and temp_obj.password == req_body['pass']:
            send = self.compile_req(temp_obj)
            self.status = 200
        else:
            self.status = 403
        return json.dumps(send)