from django.shortcuts import reverse
from django.views.generic import CreateView

from ..models.meal_type import MealType
from ..forms.create_meal_type import CreateNewMealType


class CreateNewMealTypeView(CreateView):
    model = MealType
    form_class = CreateNewMealType
    template_name = 'add_meal_type.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meal_types')



