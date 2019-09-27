from django.shortcuts import render
from bugbashapp.firebase import FirebaseDB
from django.contrib import auth


# Create your views here.

def signIn(request):
    return render(request, "signIn.html")

def postSignIn(request):
    email = request.POST.get('pass')
    passw = request.POST.get('pass')
    try:
        user = FirebaseDB.authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html", {"messg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')


def signUp(request):
    return render(request, "signup.html")


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = FirebaseDB.authe.create_user_with_email_and_password(email, passw)
    except:
        message = "Unable to create account try again"
        return render(request, "signup.html", {"messg": message})
        uid = user['localId']
    data = {"name": name, "status": "1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")