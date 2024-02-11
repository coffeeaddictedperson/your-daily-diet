from django.shortcuts import render

from ..models.meal_type import MealType

def meal_types(request):
    data = MealType.objects.all()
    return render(
        request=request,
        template_name='meal_types.html',
        context={
            'types_data': data,
            'user': request.user
        }
    )
