import uuid
from django.db import models

from ..utils.meal_types import MEAL_TYPES


class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=1, choices=MEAL_TYPES,
                                 default='D', blank=False, null=False)
    is_vegetarian = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.meal_type}"

    def update_type(self, new_type):
        self.meal_type = new_type
        self.save()
