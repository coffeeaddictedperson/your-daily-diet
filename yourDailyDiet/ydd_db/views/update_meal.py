from django.shortcuts import reverse
from django.views.generic import UpdateView

from ..models.meal import Meal
from ..forms.update_meal import UpdateMeal


class UpdateMealView(UpdateView):
    model = Meal
    form_class = UpdateMeal
    template_name = 'update_meal.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meals_list')



