from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .bot_methods import create_bot_user, create_or_update_bot_user
from ..forms.register import LoginForm, SignupForm
from ..models.bot_data import BotUserData


# login page
def user_login(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                create_or_update_bot_user(user, form)
                return redirect('profile')
    elif request.method == 'GET':
        initial = {
            'bot_username': request.GET.get('username'),
            'bot_user_id': request.GET.get('userid'),
        }
        form = LoginForm(initial=initial)
    return render(request, 'registration/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_profile(request):
    bot_user = BotUserData.objects.filter(user=request.user).first()

    return render(
        request=request,
        template_name='registration/profile.html',
        context={
            'user': request.user,
            'name': request.user.username,
            'bot_user': bot_user,
        }
    )


def user_signup(request):
    logout(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                create_bot_user(user, form)
                return redirect('profile')
    elif request.method == 'GET':
        initial = {
            'bot_username': request.GET.get('username'),
            'bot_user_id': request.GET.get('userid'),
        }
        form = SignupForm(initial=initial)

    return render(request, 'registration/signup.html', {'form': form})
