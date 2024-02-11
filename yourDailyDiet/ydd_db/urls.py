from django.urls import path

from .views.main_page import main_page
from .views.create_meal import CreateNewMealView
from .views.meals_list import meals_list

urlpatterns = [
    path("", main_page, name="main"),
    path('add-meal/',  CreateNewMealView.as_view(),  name='add_meal'),
    path('meals/',  meals_list,  name='meals_list'),
]