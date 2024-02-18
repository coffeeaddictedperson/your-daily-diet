from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..models.bot_data import BotUserData


def delete_integration(request):
    bot_user = BotUserData.objects.filter(user=request.user).first()
    if bot_user:
        bot_user.delete()
    return redirect('profile')


def create_bot_user(user, form):
    bot_username = form.cleaned_data['bot_username']
    bot_user_id = form.cleaned_data['bot_user_id']

    if bot_username and bot_user_id:
        bot_user = BotUserData.objects.create(
            user=user,
            bot_username=bot_username,
            bot_user_id=bot_user_id,
        )
        bot_user.save()
        bot_user.update_bot_code()

def create_or_update_bot_user(user, form):
    bot_username = form.cleaned_data['bot_username']
    bot_user_id = form.cleaned_data['bot_user_id']

    if bot_username and bot_user_id:
        bot_user = BotUserData.objects.filter(user=user).first()
        if bot_user:
            bot_user.update_bot_code()
        else:
            create_bot_user(user, form)


@login_required(login_url='login')
def generate_new_code(request):
    bot_user = BotUserData.objects.filter(user=request.user).first()
    if bot_user:
        bot_user.update_bot_code()
    return redirect('profile')
