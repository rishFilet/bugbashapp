from django.shortcuts import render, redirect
from .forms import UserForm
import pyrebase

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

def signup(request):
    user_form = UserForm(data = request.POST)
    return render(request, 'signUp.html', {'user_form': user_form})

def postsignup(request):
    user_form = UserForm(data = request.POST)
    if user_form.is_valid():
        try:
            user = authe.create_user_with_email_and_password(user_form.data.get('email'),
                                                                          user_form.data.get(
                                                                              'password'))
            uid = user['localId']
            print("successfully creating db")
        except:
            message = "Unable to create account try again"
            return redirect('/signup/')
            print("NOT creating db")

        data = {"First": user_form.data.get('first_name'), "Last": user_form.data.get('last_name'),"Email": user_form.email, "Role": user_form.data.get('role')}
        database.child("users").child(uid).child("details").set(data)
        return render(request, "login.html")
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    #  registered = False
    #
    # # If it's a HTTP POST, we're interested in processing form data.
    # if request.method == 'POST':
    #     # Attempt to grab information from the raw form information.
    #     # Note that we make use of both UserForm and UserProfileForm.
    #     user_form = UserForm(data=request.POST)
    #     #profile_form = UserProfileForm(data=request.POST)
    #
    #     # If the two forms are valid...
    #     if user_form.is_valid(): #and profile_form.is_valid():
    #         # Save the user's form data to the database.
    #         #user = user_form.save()
    #         try:
    #             userDB = FirebaseDB().authe.create_user_with_email_and_password(user_form.email,
    #                                                                             user_form.password)
    #             uid = userDB['localId']
    #             data = {"First": user_form.data.get('first_name'), "Last": user_form.data.get(
    #                 'last_name'),
    #                     "Email": user_form.email, "Role": user_form.data.get('role')}
    #             FirebaseDB().database.child("users").child(uid).set(data)
    #         except:
    #             message = "Unable to create account try again"
    #             return render(request, "signup.html", {"messg": message})
    #         # Now we hash the password with the set_password method.
    #         # Once hashed, we can update the user object.
    #         #user.set_password(user.password)
    #         #user.save()
    #
    #         # Now sort out the UserProfile instance.
    #         # Since we need to set the user attribute ourselves, we set commit=False.
    #         # This delays saving the model until we're ready to avoid integrity problems.
    #         # profile = profile_form.save(commit=False)
    #         # profile.user = user
    #
    #         # Now we save the UserProfile model instance.
    #         # profile.save()
    #         registered = True
    #         return redirect('/login/')
    #         #return render(request,'login.html', )
    #         #database.child("users").child(uid).child("details").set(data)
    #         # Update our variable to tell the template registration was successful.
    #
    #     # Invalid form or forms - mistakes or something else?
    #     # Print problems to the terminal.
    #     # They'll also be shown to the user.
    #     else:
    #         print(user_form.errors )#profile_form.errors)
    #
    #     # Not a HTTP POST, so we render our form using two ModelForm instances.
    #     # These forms will be blank, ready for user input.
    #     else:
    #         user_form = UserForm()
    #         #profile_form = UserProfileForm()
    #
    #     # Render the template depending on the context.
    #     return render(request, 'signUp.html', {'user_form': user_form,
    #                                            'registered': registered})