from django.shortcuts import reverse
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..models.meal import Meal
from ..forms.create_meal import CreateNewMeal




@method_decorator(login_required, name='dispatch')
class CreateNewMealView(CreateView):
    model = Meal
    form_class = CreateNewMeal
    template_name = 'add_meal.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meals_list')



