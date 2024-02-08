from django import forms

from .models import Meal

class CreateNewMeal(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'meal_description', 'meal_type', 'is_vegetarian']
        labels = {
            'meal_name': 'Meal Name',
            'meal_description': 'Description',
            'meal_type': 'Type',
            'is_vegetarian': 'Vegetarian'
        }
        help_texts = {
            'meal_name': 'Enter the name of the meal',
            'meal_description': 'Enter a brief description of the meal',
            'meal_type': 'Select the type of meal',
            'is_vegetarian': 'Check if the meal is vegetarian'
        }
        error_messages = {
            'meal_name': {
                'max_length': "This meal's name is too long."
            }
        }