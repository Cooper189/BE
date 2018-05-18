from django.db import models

class Records(models.Model):
    user_id = models.CharField(max_length=50)
    startDate = models.DateTimeField('date published')
    title = models.CharField(max_length = 250)
    article = models.TextField()
