from django.shortcuts import reverse
from django.views.generic import DeleteView

from ..models.meal import Meal


class DeleteMealView(DeleteView):
    model = Meal
    template_name = 'delete_meal.html'

    def get_success_url(self):
        return reverse('meals_list')



