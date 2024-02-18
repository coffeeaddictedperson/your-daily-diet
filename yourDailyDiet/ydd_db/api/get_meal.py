from random import choice
from django.http import JsonResponse

from .bot_user import BotUserAPI, USER_VERIFIED
from ..models.meal import Meal
from ..models.meal_type import MealType


def get_random_meal(request):
    request_type = request.GET.get('type')
    user_id = request.GET.get('user_id')

    user_status = BotUserAPI.verify_user(user_id, True)

    if user_status != USER_VERIFIED:
        return JsonResponse({"meal": None, "user_status": user_status}, safe=False)

    available_types = []
    if request_type is not None:
        available_types = MealType.objects.filter(
            name__icontains=request_type.lower())

    random_pk = None
    if len(available_types) > 0:
        pks = Meal.objects.filter(type=available_types[0].pk).values_list(
            'pk', flat=True)
        random_pk = choice(pks) if pks.count() > 0 else None

    if random_pk is None:
        return JsonResponse({"meal": None, "user_status": user_status}, safe=False)
    else:
        random_meal = Meal.objects.get(pk=random_pk)
        return JsonResponse({
            "meal": random_meal.name,
            "description": random_meal.description,
            "is_vegetarian": random_meal.is_vegetarian,
            "user_status": user_status
        }, safe=False)

