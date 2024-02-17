from django.urls import path, re_path

from .api.bot_user import BotUserAPI
from .api.get_meal_types import get_meal_types
from .api.get_meal import get_random_meal

from .views.registration import user_login, user_logout, user_signup

from .views.main_page import main_page
from .views.create_meal import CreateNewMealView
from .views.delete_meal import DeleteMealView
from .views.update_meal import UpdateMealView
from .views.meals_list import meals_list

from .views.create_meal_type import CreateNewMealTypeView
from .views.meal_types import meal_types


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', user_signup, name='signup'),

    path('',  meals_list,  name='main_page'),
    path('meals/',  meals_list,  name='meals_list'),

    path('meals/add', CreateNewMealView.as_view(),  name='add_meal'),
    path('meals/<uuid:pk>/delete',  DeleteMealView.as_view(),
         name='delete_meal'),
    path('meals/<uuid:pk>/update',  UpdateMealView.as_view(),
         name='update_meal'),

    path('meal-types/', meal_types, name='meal_types'),
    path('meal-types/add', CreateNewMealTypeView.as_view(),  name='add_meal_type'),

    # API
    path(r"api/meal-types", get_meal_types, name='get_meal_types'),
    re_path(r"api/meal(?P<type>[\w]+)?/$", get_random_meal, name='get_meal'),

    path('api/bot-user/login/<user_id>', BotUserAPI.login_bot_user,  name='login_bot_user'),
    path('api/bot-user/logout/<user_id>', BotUserAPI.login_bot_user,
         name='logout_bot_user'),
    path('api/bot-user/delete/<user_id>', BotUserAPI.delete_bot_user,
         name='delete_bot_user'),
]