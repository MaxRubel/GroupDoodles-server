from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=320)
    date_registered = models.DateField(auto_now=True)
