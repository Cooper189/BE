from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from users.classes.user_data import GetUser
from users.classes.user_models import UsersData
import json

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
            'type' : 'Components',
            'url': '/user'
        },
        {
            'type' : 'Props v. State',
            'url': '/user/create'
        },
        {
            'type' : 'Main page',
            'url': '/'
        }
    ]
    return HttpResponse(json.dumps(temp_obj))
