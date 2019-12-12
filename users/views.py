from django.contrib.auth import authenticate, login, logout
from django.contrib import messages as msgs
from django.shortcuts import render, HttpResponseRedirect, redirect

from users.managers import CustomUserManager
from .forms import UserForm, UserLogin

def login_view(request):
	if request.user.is_authenticated:

		return redirect('home')
	else:
		user_login = UserLogin(data = request.POST)
		if request.method == 'POST':
			email = user_login.data.get('email')
			password = user_login.data.get('password')

			user = authenticate(request, username=email, password=password)

			if user is not None:
				login(request, user)
				msgs.success(request, 'Welcome {} to the Bug bash'.format(user.first_name))
				return HttpResponseRedirect('/home/')
			else:
				msgs.error(request, 'Error: Wrong username/password')
				return render(request, 'login.html', {'user_login': user_login})

		else:
			return render(request, 'login.html',  {'user_login': user_login})

def logout_view(request):
	logout(request)
	user_login = UserLogin()
	msgs.success(request, 'You have successfully logged out')
	return render(request, 'login.html',  {'user_login': user_login})

def register(request):
	registered = False
	user_form = UserForm(data = request.POST)
	if request.method == 'POST':
		if user_form.is_valid():

			custom_user = CustomUserManager()
			user = custom_user.create_user(email=user_form.data.get('email'), password=user_form.data.get('password'))
			user.save()
			msgs.success(request, "Success: You are registered!")
			registered = True
			return redirect('login_view')

		else:
			try:
				print(user_form.errors['email'])
				if 'This email address is already in use' in user_form.errors['email'][0]:
					msg = "Email already registered, try logging in"
			except:
				msg = "Please try to register again!"
			user_form = UserForm()
			msgs.error(request, msg)
	else:
		user_form = UserForm()

	return render(request, "register.html", {'user_form': user_form, 'registered': registered})
