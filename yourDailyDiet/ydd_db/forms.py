from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit

from .models import Meal

class CreateNewMeal(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'meal_description', 'meal_type', 'is_vegetarian']
        labels = {
            'meal_name': 'Страва',
            'meal_description': 'Короткий опис',
            'meal_type': 'Тип страви',
            'is_vegetarian': 'Чи вегетаріанська?'
        }
        error_messages = {
            'meal_name': {
                'max_length': "This meal's name is too long."
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(
                Row('meal_name', css_class='form-group'),
                Row('meal_description', css_class='form-group col-md-6'),
                Row(
                    Column('meal_type', css_class='form'),
                    Column('is_vegetarian', css_class='form')
                ),
            ),
            Submit('submit', 'Add meal', css_class='btn btn-success')
        )