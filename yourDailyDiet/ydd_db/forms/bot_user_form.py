import uuid

from django import forms

from ..models.bot_data import BotUserData


class BotUserForm(forms.Form):
    class Meta:
        model = BotUserData
        fields = ['bot_username', 'bot_user_id']

    result = uuid.uuid4()
    bot_username = forms.CharField(max_length=100, required=True)