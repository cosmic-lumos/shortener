from django.db import models

# Create your models here.

class URL(models.Model):
    origin = models.CharField(max_length=1000, unique=True, db_index=True)
    shortened = models.CharField(max_length=8, unique=True)
    expire = models.DateField()