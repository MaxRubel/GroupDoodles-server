from django.db import models
from .user import User

class Doodle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
    data = models.JSONField()
    collaborators = models.ManyToManyField(User, through="DoodleCollab", related_name="doodles")