from django.db import models
from .user import User

class Palette(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    colors = models.JSONField()
    date_created = models.DateField(auto_now=True)
    liked_by = models.ManyToManyField(User, through="PaletteLike", related_name="palettes")