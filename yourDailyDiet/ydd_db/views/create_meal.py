from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import reverse
from django.views.generic import CreateView

from ..forms.create_meal import CreateNewMeal
from ..models.meal import Meal


class CreateNewMealView(PermissionRequiredMixin, CreateView):
    model = Meal
    form_class = CreateNewMeal
    template_name = 'add_meal.html'
    permission_required = 'ydd_db.add_meal'


    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meals_list')



