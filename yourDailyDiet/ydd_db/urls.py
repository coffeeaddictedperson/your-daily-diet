from django.urls import path

from .views.main_page import main_page
from .views.create_meal import CreateNewMealView
from .views.delete_meal import DeleteMealView
from .views.update_meal import UpdateMealView
from .views.meals_list import meals_list

from .views.create_meal_type import CreateNewMealTypeView
from .views.meal_types import meal_types

urlpatterns = [
    # path("", main_page, name="main"),
    path('',  meals_list,  name='meals_list'),
    path('meals/',  meals_list,  name='meals_list'),

    path('meals/add', CreateNewMealView.as_view(),  name='add_meal'),
    path('meals/<uuid:pk>/delete',  DeleteMealView.as_view(),
         name='delete_meal'),
    path('meals/<uuid:pk>/update',  UpdateMealView.as_view(),
         name='update_meal'),

    path('meal-types/', meal_types, name='meal_types'),
    path('meal-types/add', CreateNewMealTypeView.as_view(),  name='add_meal_type'),
]