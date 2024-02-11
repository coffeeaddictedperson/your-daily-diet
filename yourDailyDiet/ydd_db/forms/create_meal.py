from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit

from .meal_labels import LABELS, WARNINGS
from ..models.meal import Meal


class CreateNewMeal(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'type', 'is_vegetarian']
        labels = LABELS
        error_messages = WARNINGS
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
                    Column('type', css_class='form col-md-6'),
                    Column('is_vegetarian', css_class='form col-md-6')
                ),
            )
        )
