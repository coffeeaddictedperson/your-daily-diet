from django.shortcuts import render, redirect
from django.views.generic import CreateView

from ..models.meal import Meal
from ..forms.create_meal import CreateNewMeal


class CreateNewMealView(CreateView):
    model = Meal
    form_class = CreateNewMeal
    template_name = 'add_meal.html'

    def form_valid(self, form):
        # form.instance.author = Author.objects.first()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('news')



