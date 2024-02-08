from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path('add-meal/',  views.CreateNewMealView.as_view(),  name='add_meal'),
]