from random import choice
from django.http import JsonResponse

from ..models.meal import Meal
from ..models.meal_type import MealType


def get_random_meal(request):
    request_type = request.GET.get('type')

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
        return JsonResponse({"name": None}, safe=False)
    else:
        random_meal = Meal.objects.get(pk=random_pk)
        return JsonResponse({"meal": random_meal.name}, safe=False)

