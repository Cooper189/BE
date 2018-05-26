from classes.rest import RestFullAPI
from records.models import Records
import json
from django.utils import timezone
from users.models import Users


class RecordResponse(RestFullAPI):
    def __init__(self):
        super(RecordResponse, self).__init__()

    def get_request(self, req):
        query_params = req.GET.get('userId', '')
        data_from = Records.objects.filter(user_id=query_params)
        send_from = []
        for info in data_from:
            send_from.append({
                'recordId': info.id,
                'userId': info.user_id,
                'startDate': info.startDate.timestamp() * 1000,
                'title': info.title})
        return json.dumps(send_from)
    
    def post_request(self, req):
        post_body = json.loads(req.body)
        try:
            temp = Users.objects.get(id=post_body['userId'])
            temp_db = Records(
                user_id=post_body['userId'], 
                startDate=timezone.now(),
                title=post_body['title'], 
                article=post_body['article'], 
                user_name=temp.user_name
            )
            temp_db.save()
            self.status = 200
            return 'done'
        except Exception as err:
            self.status = 403
            return err
