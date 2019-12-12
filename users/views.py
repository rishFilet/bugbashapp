from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login as auth_login
from .forms import UserLogin, RegisterForm


def login_view(request):
    user_login = UserLogin(data=request.POST)
    if request.method == 'POST':
        email = user_login.data.get('email')
        password = user_login.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')

    else:
        return render(request, 'login.html', {'user_login': user_login})


def sign_up(request):
    form = UserCreationForm()
    return render(request, "register.html", {'form': form})


def register(request):
    register_form = RegisterForm(data=request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            user = register_form.save()
            auth_login(request, user)
            return HttpResponseRedirect('/home/', "Success: You are registered!")

    else:
        register_form = RegisterForm()
    return render(request, "register.html", {'form': register_form})
