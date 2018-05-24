from django.shortcuts import render
from django.http import HttpResponse
from classes.rest import RestFullAPI
from django.views.decorators.csrf import csrf_exempt
from records.models import Records
from records.methods.all import AllRecord
from records.methods.record import RecordResponse
from records.methods.single import SingleRecord
import json

record_api = RecordResponse()
single_record_api = SingleRecord()
all_record_api = AllRecord()

@csrf_exempt
def get_all_record(request):
    return HttpResponse(all_record_api.rest(request), status=all_record_api.status, content_type=all_record_api.get_type)
@csrf_exempt
def index(request):
    return HttpResponse(record_api.rest(request), status=record_api.status, content_type=record_api.get_type)
@csrf_exempt
def single(request):
    return HttpResponse(single_record_api.rest(request), status=single_record_api.status, content_type=single_record_api.get_type)