from django import forms

from django.utils.translation import gettext
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit

from ..models.meal import Meal


class CreateNewMeal(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'meal_type', 'is_vegetarian']
        labels = {
            'name': gettext('Meal'),
            'description': gettext('Short description'),
            'meal_type': gettext('Better for...'),
            'is_vegetarian': gettext('Vegetarian?')
        }
        error_messages = {
            'name': {
                'max_length': "This meal's name is too long."
            }
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(
                Row('name', css_class='form-group'),
                Row('description', css_class='form-group col-md-6'),
                Row(
                    Column('meal_type', css_class='form'),
                    Column('is_vegetarian', css_class='form')
                ),
            ),
            Submit('submit', 'Add meal', css_class='btn btn-success')
        )
