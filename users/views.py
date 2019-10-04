from django.shortcuts import render, redirect
from .forms import UserForm
import pyrebase


#Firebase databse information and setup
config = {
    'apiKey': "AIzaSyBprp7rJwq64GaMhbX-5ST2wb7PS43IVZw",
    'authDomain': "bugbash-b4d18.firebaseapp.com",
    'databaseURL': "https://bugbash-b4d18.firebaseio.com",
    'projectId': "bugbash-b4d18",
    'storageBucket': "",
    'messagingSenderId': "356090318351",
    'appId': "1:356090318351:web:e865ba40d674301fe59d7a",
    'measurementId': "G-FQR855D0DY"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def login(request):
    return render(request, 'login.html')


def register(request):
    user_form = UserForm(data = request.POST)
    return render(request, 'register.html', {'user_form': user_form})


def post_register(request):
    user_form = UserForm(data = request.POST)
    if user_form.is_valid():
        try:
            user = authe.create_user_with_email_and_password(user_form.data.get('email'),
                                                                          user_form.data.get(
                                                                              'password'))
            uid = user['localId']
        except:
            message = "Unable to create account try again"
            return redirect('/register/', {'message': message})

        #Add data from user_form to a dictionary
        data = {"First": user_form.data.get('first_name'), "Last": user_form.data.get('last_name'),"Email": user_form.email, "Role": user_form.data.get('role')}

        #Add dictionary details of user to the database
        database.child("users").child(uid).child("details").set(data)

        return render(request, "login.html")
