import uuid
from django.db import models


class BotUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=20, unique=True)
    bot_user_id = models.IntegerField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    logged_in = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
