from classes.rest import RestFullAPI

class PermanentObj(RestFullAPI):
    def compile_req(self, obj):
        return {
                'userId': str(obj.id),
                'login': obj.user_login,
                'name': obj.user_name,
                'startDate': obj.startDate.timestamp() * 1000,
                'mail': obj.email
            }