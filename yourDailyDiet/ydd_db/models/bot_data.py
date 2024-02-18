import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def generate_valid_till():
    return timezone.now() + timezone.timedelta(days=10)


class BotUserData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    bot_username = models.CharField(max_length=100, null=False, blank=False)
    bot_user_id = models.CharField(max_length=100, unique=True)
    bot_created_at = models.DateTimeField(auto_now_add=True)

    bot_updated_at = models.DateTimeField(auto_now=True)

    bot_valid_till = models.DateTimeField(auto_now_add=True)
    bot_code = models.CharField(max_length=20, unique=True)
    is_verified = models.BooleanField(default=False)

    is_suspended = models.BooleanField(default=False)
    requests_count = models.IntegerField(default=0)


    class Meta:
        ordering = ["bot_valid_till"]

    def __str__(self):
        return f'{self.bot_username}({self.bot_user_id})'

    @property
    def is_expired(self):
        return self.bot_valid_till < timezone.now()

    @property
    def is_verified_and_valid(self):
        return not self.is_expired and self.is_verified

    def update_bot_code(self):
        self.bot_code = uuid.uuid4().hex[:20]
        self.bot_valid_till = generate_valid_till()
        self.is_verified = False
        self.save()

    def is_valid_code(self, code):
        return self.bot_code == code

    def set_is_verified(self):
        self.is_verified = True
        self.save()

    def update_requests_count(self):
        self.requests_count += 1
        self.save()