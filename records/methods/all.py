from classes.rest import RestFullAPI
from records.models import Records
import json
from django.utils import timezone

class AllRecord(RestFullAPI):
    def get_request(self, req):
        data_from = Records.objects.all()[:5]
        send_from = []
        for info in data_from:
            send_from.append({
                'recordId': info.id,
                'userId': info.user_id,
                'startDate': info.startDate.timestamp() * 1000,
                'title': info.title})
        return json.dumps(send_from)