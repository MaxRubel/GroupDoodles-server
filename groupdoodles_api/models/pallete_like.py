from django.db import models
from .user import User
from .palette import Palette

class PaletteLike(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    palette=models.ForeignKey(Palette, on_delete=models.CASCADE)
    