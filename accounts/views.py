from django.contrib import messages as msgs
from django.contrib.auth import authenticate, logout, login as auth_login
from django.shortcuts import render, HttpResponseRedirect, redirect

from utils import clear_messages as clr
from .forms import UserLogin, RegisterForm
from .models import CustomUser


def login_view(request):
    clr.clear_msgs(request)
    if request.user.is_authenticated:
        return redirect('/bugreport/')
    else:
        user_login = UserLogin(data = request.POST)
        if request.method == 'POST':
            email = user_login.data.get('email')
            password = user_login.data.get('password')
            user = authenticate(request, username = email, password = password)
            if user is not None:
                auth_login(request, user)
                msgs.success(request, 'Welcome to the Bug bash {}'.format(user.first_name))
                return HttpResponseRedirect('/bugreport/')

            elif CustomUser.objects.filter(email = email).exists():
                msgs.error(request, 'Wrong password for user: {}'.format(email))
                return render(request, 'login.html', {'user_login': user_login})
            else:
                msgs.error(request, 'Error: User not registered')
                return render(request, 'login.html', {'user_login': user_login})
        else:
            return render(request, 'login.html', {'user_login': user_login})


def logout_view(request):
    logout(request)
    user_login = UserLogin()
    msgs.success(request, 'You have successfully logged out')
    return render(request, 'login.html', {'user_login': user_login})


def register(request):
    register_form = RegisterForm(data = request.POST)
    if request.method == 'POST':
        msg = "Unable to create account"
        if register_form.is_valid():
            user = register_form.save()
            auth_login(request, user)
            msgs.success(request, "Success: You are registered!")
            return HttpResponseRedirect('/bugreport/')
        else:
            try:
                if 'This email address is already in use' in register_form.errors['email'][0]:
                    msg = "Email already registered, try logging in"
            except:
                msg = "Please try to register again!"
            msgs.error(request, msg)
    else:
        register_form = RegisterForm()
    return render(request, "register.html", {'form': register_form})
