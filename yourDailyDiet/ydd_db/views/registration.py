from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ..forms.register import UserCreationForm, LoginForm


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})