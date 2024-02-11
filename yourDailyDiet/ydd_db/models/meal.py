import uuid
from django.db import models
from ..models.meal_type import MealType

class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    type = models.ForeignKey(to=MealType, on_delete=models.CASCADE,
                             default=None)
    is_vegetarian = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.type}"
