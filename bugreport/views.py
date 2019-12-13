import time
from datetime import datetime, timezone

import pytz
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bugbashapp.firebase import FirebaseDB as fdb
from . import models


# Create your views here.
def create_report(request):
    submitted = False
    if request.method == 'POST':
        form = models.BugLogForm(request.POST)
        if form.is_valid():

            try:

                message = "SUCCESS: Bug Report Submitted"
                tz = pytz.timezone('US/Eastern')
                current_time = datetime.now(timezone.utc).astimezone(tz)
                millis = int(time.mktime(current_time.timetuple()))
                idToken = request.session['uid']
                user_info = fdb.authe.get_account_info(idToken)

                # Add data from BugLogForm to a dictionary
                data = {
                    "Device": form.data.get("device"),
                    "Feature": form.data.get("feature"),
                    "Summary": form.data.get("summary"),
                    "Steps": form.data.get("steps"),
                    "Result": form.data.get("result")
                }
                form.save()
                # Add dictionary data to the database
                localId = user_info['accounts'][0]['localId']
                fdb.database.child("accounts").child(localId).child("reports").child(millis).set(data)
                return HttpResponseRedirect('/home/', messages.error(request, message))
            except:
                message = "ERROR: Could not log bug successfully"
                return redirect('/home/', messages.error(request, message))

            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/home?submitted=True')
    else:
        form = models.BugLogForm()

    return render(request, 'home.html', {'form': form, 'submitted': submitted})
