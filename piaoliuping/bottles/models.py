import random
from django.db import models

from ..users.models import User


class Bottle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, blank=True)
    is_read = models.BooleanField(default=False)

    @classmethod
    def pick_random_bottle(cls, user_id: int):
        """pick a unread bottle that is not yours"""
        all_bottles = cls.objects.filter(is_read=False).exclude(user=user_id).all()
        if len(all_bottles) == 0:
            return None

        random_index = random.randint(0, len(all_bottles) - 1)
        bottle = all_bottles[random_index]
        bottle.is_read = True
        bottle.save()
        return bottle
