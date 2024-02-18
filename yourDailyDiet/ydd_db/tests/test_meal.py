from django.test import TestCase, Client

from ydd_db.models.meal_type import MealType
from ydd_db.models.meal import Meal


# Create your tests here.
class MealTestCase(TestCase):
    def setUp(self):
        self.meal_type = MealType.objects.create(name='Test Meal Type')

        self.meal = Meal.objects.create(
            name='Test Meal',
            description='Test Description',
            is_vegetarian=True,
            type=self.meal_type
        )

    def test_is_vegetarian(self):
        meal = Meal.objects.first()
        self.assertTrue(meal.is_vegetarian)
        self.assertTrue(meal.type.name, 'Test Meal Type')