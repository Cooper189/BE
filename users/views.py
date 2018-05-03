from django.shortcuts import render
from classes.rest import RestFullAPI
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from users.models import Users
from django.http import HttpResponse
import json

class UsersData(RestFullAPI):
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
            temp_db = Users(user_login = post_body['login'], 
                            user_name = post_body['name'], 
                            password=post_body['pass'],
                            startDate=timezone.now(), 
                            email=post_body['email'])
            temp_db.save()
            return 'done'
        except Exception as err:
            return err

class GetUser(RestFullAPI):
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

    def compile_req(self, obj):
        return {
                'userId': str(obj.id),
                'login': obj.user_login,
                'name': obj.user_name,
                'startDate': obj.startDate.timestamp() * 1000,
                'mail': obj.email
            }


temp_rest_api = UsersData()
temp_rest = GetUser()

@csrf_exempt
def set_users(request):
    return HttpResponse(temp_rest_api.rest(request), status=temp_rest_api.status, content_type=temp_rest_api.get_type)

@csrf_exempt
def get_users(request):
    return HttpResponse(temp_rest.rest(request),status=temp_rest.status, content_type=temp_rest.get_type)

@csrf_exempt
def test(request):
    temp_obj = [
        {
            'type': 'Rendering with React',
            'url': '/'
        },
        {
            'type' : 'Components',
            'url': '/art'
        },
        {
            'type' : 'Props v. State',
            'url': '/art/info'
        }
    ]
    return HttpResponse(json.dumps(temp_obj))
