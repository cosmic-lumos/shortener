from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.CharField(max_length=1000, )
    shortened = models.CharField(max_length=5 )