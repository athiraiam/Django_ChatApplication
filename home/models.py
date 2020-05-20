from django.db import models

# Create your models here.
class SearchModel(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)