from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm, UserLogin
import pyrebase


#Firebase databse information and setup
config = {
  "apiKey": "AIzaSyBprp7rJwq64GaMhbX-5ST2wb7PS43IVZw",
  "authDomain": "bugbash-b4d18.firebaseapp.com",
  "databaseURL": "https://bugbash-b4d18.firebaseio.com/",
  "storageBucket": "bugbash-b4d18.appspot.com",
}


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def login(request):
    user_login = UserLogin(data=request.POST)
    return render(request, 'login.html', {'user_login': user_login})


def post_login(request):
    user_login = UserLogin(data=request.POST)
    email = user_login.data.get('email')
    password = user_login.data.get('password')
    try:
        user = authe.sign_in_with_email_and_password(email, password)
    except:
        message = "Wrong email or password"
        messages.error(request, message)
        return render(request, "login.html")
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    #return render(request, "welcome.html", {"e": email})
    return render(request, 'home.html', {'user_login': user_login})


def register(request):
    registered = False
    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        if user_form.is_valid():
            try:
                user = authe.create_user_with_email_and_password(user_form.data.get('email'),
                                                                 user_form.data.get(
                                                                     'password'))
                uid = user['localId']
                message = "Success: You are registered!"
                # Add data from user_form to a dictionary
                data = {"First": user_form.data.get('first_name'),
                        "Last": user_form.data.get('last_name'), "Email": user_form.data.get(
                        'email'),
                        "Role": user_form.data.get('role')}

                # Add dictionary details of user to the database
                database.child("users").child(uid).child("details").set(data, user['idToken'])
                return HttpResponseRedirect('/login/', messages.error(request, message))
            except:
                message = "Email is already registered. Try logging in"
                return redirect('/register/', messages.error(request, message))


        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, "register.html", {'user_form': user_form, 'registered': registered})
