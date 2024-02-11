from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row

from .meal_type_labels import LABELS, WARNINGS
from ..models.meal_type import MealType


class CreateNewMealType(forms.ModelForm):
    class Meta:
        model = MealType
        fields = ['name', 'description']
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
            )
        )
