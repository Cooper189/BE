from django.utils import timezone
from users.classes.helper import PermanentObj
from users.models import Users
import json

class UsersData(PermanentObj):
    def __init__(self):
        super(UsersData, self).__init__()

    def get_request(self):
        data_from = Users.objects.all()
        send_from = []
        for info in data_from:
            send_from.append({
                'name': info.user_name,
                'startDate': info.startDate.timestamp() * 1000,
                'mail': info.email})
        return json.dumps(send_from)


    def post_request(self, req):
        post_body = json.loads(req.body)
        try:
            temp_db = Users(
                user_login = post_body['login'], 
                user_name = post_body['name'], 
                password=post_body['pass'],
                startDate=timezone.now(), 
                email=post_body['email']
            )
            temp_db.save()
            temp_obj = Users.objects.get(user_login = post_body['login'])
            send = self.compile_req(temp_obj)
            return json.dumps(send)
        except Exception as err:
            return err