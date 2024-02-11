from django.urls import path

from .views.main_page import main_page
from .views.create_meal import CreateNewMealView

urlpatterns = [
    path("", main_page, name="main"),
    path('add-meal/',  CreateNewMealView.as_view(),  name='add_meal'),
]