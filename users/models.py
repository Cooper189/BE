from django.db import models

class Users(models.Model):
    user_login = models.CharField(max_length=50)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 20)
    startDate = models.DateTimeField('date published')
    user_name = models.CharField(max_length = 100)

