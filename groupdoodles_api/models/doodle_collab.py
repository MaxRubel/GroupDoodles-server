from django.db import models
from .user import User
from .doodle import Doodle
from .user import User

class DoodleCollab(models.Model):
    doodle = models.ForeignKey(Doodle, on_delete=models.CASCADE, related_name="doodle_collabs")
    collab = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doodle_collabs")