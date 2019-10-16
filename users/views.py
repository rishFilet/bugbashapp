from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm, UserLogin
from .models import models
from bugbashapp.firebase import FirebaseDB as fdb
import json


def login(request):
	user_login = UserLogin(data = request.POST)
	if request.method == 'POST':
		email = user_login.data.get('email')
		password = user_login.data.get('password')

		try:
			user = fdb.authe.sign_in_with_email_and_password(email, password)
			message = "WELCOME TO THE BUG BASH {}".format(fdb.database.child("users").child(user[
			'localId']).child("details").child("First").get().val().capitalize())
			# user_login.save()

		except Exception as e:
			error_json = e.args[1]
			error = json.loads(error_json)['error']
			print(error['message'])
			if "INVALID_PASSWORD" in error['message']:
				message = "Wrong password. Please try again."
				return redirect('/login/', messages.error(request, message))
			else:
				message = "Email address not registered. Please register."
				return redirect('/register/', messages.error(request, message))
		return HttpResponseRedirect('/home/', messages.error(request, message))
		session_id = user['idToken']
		request.session['uid'] = str(session_id)
	else:
		return render(request, 'login.html', {'user_login': user_login})


def register(request):
	registered = False
	user_form = UserForm(data = request.POST)
	if request.method == 'POST':

		if user_form.is_valid():
			try:
				user = fdb.authe.create_user_with_email_and_password(user_form.data.get('email'),
																 user_form.data.get(
																	 'password'))
				uid = user['localId']
				message = "Success: You are registered!"
				# Add data from user_form to a dictionary
				data = {"First": user_form.data.get('first_name'),
						"Last": user_form.data.get('last_name'), "Email": user_form.data.get(
						'email'),
						"Role": user_form.data.get('role')}
				user_form.save()

				# Add dictionary details of user to the database
				fdb.database.child("users").child(uid).child("details").set(data, user['idToken'])
				return HttpResponseRedirect('/login/', messages.error(request, message))
			except Exception as e:
				error_json = e.args[1]
				error = json.loads(error_json)['error']
				print(error['message'])
				if "EMAIL_EXISTS" in error['message']:
					message = "Email is already registered. Try logging in"
				else:
					message = "Something went wrong. Please try again later"
				return redirect('/register/', messages.error(request, message))


		else:
			print(user_form.errors)

	else:
		user_form = UserForm()

	return render(request, "register.html", {'user_form': user_form, 'registered': registered})
