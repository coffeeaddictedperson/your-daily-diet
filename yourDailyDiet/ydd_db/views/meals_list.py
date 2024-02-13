from django.shortcuts import render

from ..models.meal import Meal

def meals_list(request):
    data = Meal.objects.all()
    print(request.user)
    return render(
        request=request,
        template_name='meals_list_page.html',
        context={
            'meals_data': data,
            'user': request.user
        }
    )
