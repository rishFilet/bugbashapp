from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from bugbashapp.firebase import FirebaseDB as fdb


# Create your views here.
def create_report(request):
    submitted = False
    if request.method == 'POST':
        form = models.BugLogForm(request.POST)
        if form.is_valid():
            # try:
            #     message = "Success: You are registered!"
            #     # Add data from user_form to a dictionary
            #     data = {"First": user_form.data.get('first_name'),
            #             "Last": user_form.data.get('last_name'), "Email": user_form.data.get(
            #             'email'),
            #             "Role": user_form.data.get('role')}
            #
            #     # Add dictionary details of user to the database
            #     database.child("users").child(uid).child("details").set(data, user['idToken'])
            #     return HttpResponseRedirect('/login/', messages.error(request, message))
            # except:
            #     message = "Email is already registered. Try logging in"
            #     return redirect('/register/', messages.error(request, message))

            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/home?submitted=True')
    else:
        form = models.BugLogForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home.html', {'form': form, 'submitted': submitted})
