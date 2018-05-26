from classes.rest import RestFullAPI
from records.models import Records
import json
from django.utils import timezone

class AllRecord(RestFullAPI):
    def get_request(self, req):
        data_from = Records.objects.all()
        send_from = []
        if len(data_from) > 10:
            number = len(data_from)-10
        else:
            number = 0
        for info in data_from[number:]:
            send_from.append({
                'recordId': info.id,
                'userId': info.user_id,
                'userName': info.user_name,
                'startDate': info.startDate.timestamp() * 1000,
                'title': info.title
            })
        return json.dumps(send_from)