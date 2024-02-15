from random import choice
from django.http import JsonResponse

from ..models.meal import Meal
from ..models.meal_type import MealType


def get_random_meal(request):
    request_type = request.GET.get('type')

    if request_type is not None:
        available_types = MealType.objects.filter(
            name__icontains=request_type.lower())
    else:
        available_types = []

    if len(available_types) > 0:
        pks = Meal.objects.filter(type=available_types[0].pk).values_list(
            'pk', flat=True)
    else:
        pks = Meal.objects.values_list('pk', flat=True)

    if pks.count() == 0:
        return JsonResponse({"name": "No meals in database"}, safe=False)
    else:
        random_pk = choice(pks)
        random_meal = Meal.objects.get(pk=random_pk)
        return JsonResponse({"name": random_meal.name}, safe=False)

