from django.shortcuts import render
from django.http import HttpResponse
from classes.rest import RestFullAPI
from django.views.decorators.csrf import csrf_exempt
from records.models import Records
from django.utils import timezone
import json

class RecoreResponse(RestFullAPI):
    def __init__(self):
        super(RecoreResponse, self).__init__()

    def get_request(self, req):
        query_params = req.GET.get('userId', '')
        data_from = Records.objects.filter(user_id=query_params)
        send_from = []
        for info in data_from:
            send_from.append({
                'userId': info.user_id,
                'startDate': info.startDate.timestamp() * 1000,
                'title': info.title})
        return json.dumps(send_from)
    
    def post_request(self, req):
        post_body = json.loads(req.body)
        try:
            temp_db = Records(user_id=post_body['userId'], startDate=timezone.now(),title=post_body['title'], article=post_body['article'])
            temp_db.save()
            self.status = 200
            return 'done'
        except Exception as err:
            self.status = 403
            return err

record_api = RecoreResponse()

@csrf_exempt
def index(request):
    return HttpResponse(record_api.rest(request), status=record_api.status, content_type=record_api.get_type)
