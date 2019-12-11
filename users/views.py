from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect

from users.managers import CustomUserManager
from .forms import UserForm, UserLogin


def login_view(request):
	user_login = UserLogin(data = request.POST)
	if request.method == 'POST':
		email = user_login.data.get('email')
		password = user_login.data.get('password')

		user = authenticate(request, username=email, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/home/')

	else:
		return render(request, 'login.html', {'user_login': user_login})


def register(request):
	registered = False
	user_form = UserForm(data = request.POST)
	if request.method == 'POST':

		if user_form.is_valid():

			custom_user = CustomUserManager()
			user = custom_user.create_user(email=user_form.data.get('email'), password=user_form.data.get('password'))
			user.save()
			print(user.email)

			return HttpResponseRedirect('/login/', "Success: You are registered!")


	else:
		user_form = UserForm()

	return render(request, "register.html", {'user_form': user_form, 'registered': registered})
