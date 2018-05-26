from classes.rest import RestFullAPI
from records.models import Records
import json
from django.utils import timezone

class SingleRecord(RestFullAPI):
    def get_request(self, req):
        query_params = req.GET.get('recordId', '')
        record = Records.objects.get(id=query_params)
        return json.dumps({
            'recordId': record.id,
            'userId': record.user_id,
            'startDate': record.startDate.timestamp() * 1000,
            'title': record.title,
            'article': record.article,
            'userName': record.user_name
        })

    def put_request(self, req):
        post_body = json.loads(req.body)
        record = Records.objects.get(id=post_body['recordId'])
        record.title = post_body['title']
        record.article = post_body['article']
        record.save()
        return 'done'

    def delete_request(self, req):
        post_body = json.loads(req.body)
        Records.objects.get(id=post_body['recordId']).delete()
        return str(post_body['recordId'])
