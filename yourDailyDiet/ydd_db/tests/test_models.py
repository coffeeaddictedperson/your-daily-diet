from django.contrib.auth.models import User
from django.test import TestCase, Client

from ydd_db.models.meal_type import MealType
from ydd_db.models.meal import Meal

from ydd_db.models.bot_data import BotUserData


# Dummy initial test, nothing interesting actually
class MealModelTestCase(TestCase):
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


# Real test for the bot data
class BotDataTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.bot_user = BotUserData.objects.create(
            user=self.user,
            bot_username='test_bot',
            bot_user_id='test_bot_id',
        )

    def test_update_bot_code(self):
        bot_user = BotUserData.objects.first()
        self.assertTrue(bot_user.bot_code == '')
        bot_user.update_bot_code()
        self.assertTrue(bot_user.bot_code != '')
        self.assertTrue(bot_user.bot_valid_till != '')
        self.assertFalse(bot_user.is_verified)

    def is_valid_code(self):
        bot_user = BotUserData.objects.first()
        bot_user.update_bot_code()
        self.assertTrue(bot_user.is_valid_code(bot_user.bot_code))

    def test_set_is_verified(self):
        bot_user = BotUserData.objects.first()
        self.assertFalse(bot_user.is_verified)
        bot_user.set_is_verified()
        self.assertTrue(bot_user.is_verified)

    def test_update_requests_count(self):
        bot_user = BotUserData.objects.first()
        self.assertTrue(bot_user.requests_count == 0)
        bot_user.update_requests_count()
        bot_user.update_requests_count()
        self.assertTrue(bot_user.requests_count == 2)

    def test_is_verified_and_valid(self):
        bot_user = BotUserData.objects.first()
        bot_user.update_bot_code()
        self.assertFalse(bot_user.is_verified_and_valid)
        bot_user.set_is_verified()
        self.assertTrue(bot_user.is_verified_and_valid)
