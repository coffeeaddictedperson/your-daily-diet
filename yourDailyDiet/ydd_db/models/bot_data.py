import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BotUserData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    bot_code = models.CharField(max_length=20, unique=True)
    bot_username = models.CharField(max_length=100, null=False, blank=False)
    bot_user_id = models.CharField(max_length=100, unique=True)
    bot_created_at = models.DateTimeField(auto_now_add=True)
    bot_updated_at = models.DateTimeField(auto_now=True)
    bot_valid_till = models.DateTimeField(default=timezone.now() +
                                                  timezone.timedelta(days=10))

    class Meta:
        ordering = ["bot_valid_till"]

    def __str__(self):
        return f'{self.bot_username}({self.bot_user_id})'

    def is_still_valid(self):
        return self.bot_valid_till >= timezone.now()
