from django.shortcuts import reverse
from django.views.generic import UpdateView

from ..forms.update_meal import UpdateMeal
from ..models.meal import Meal


class UpdateMealView(UpdateView):
    model = Meal
    form_class = UpdateMeal
    template_name = 'update_meal.html'
    permission_required = 'ydd_db.update_meal'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meals_list')



