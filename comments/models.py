from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=140)
    datetime = models.DateTimeField('date published', auto_now=True)