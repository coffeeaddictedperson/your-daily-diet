from django.shortcuts import reverse
from django.views.generic import DeleteView

from ..models.meal import Meal


class DeleteMealView(DeleteView):
    model = Meal
    template_name = 'delete_meal.html'
    permission_required = 'ydd_db.delete_meal'

    def get_success_url(self):
        return reverse('meals_list')



