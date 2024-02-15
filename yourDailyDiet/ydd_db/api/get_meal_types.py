from django.http import JsonResponse

from ..models.meal_type import MealType


def get_meal_types(*args, **kwargs):
    meal_types = MealType.objects.values_list('name', flat=True)
    print(meal_types)
    return JsonResponse({"meal_types": list(meal_types)}, safe=False)
