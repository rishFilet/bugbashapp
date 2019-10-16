from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from report.models import fields
from . import models
from bugbashapp.firebase import FirebaseDB as fdb
import time
from datetime import datetime, timezone
import pytz


# Create your views here.
def create_report(request):
	submitted = False
	if request.method == 'POST':
		form = models.BugLogForm(request.POST)
		if form.is_valid():

			try:
				print("im in try block")
				message = "Bug Log Form"
				tz = pytz.timezone('US/Eastern')
				current_time = datetime.now(timezone.utc).astimezone(tz)
				millis = int(time.mktime(current_time.timetuple()))
				idToken = request.session['uid']
				print(idToken)
				print(message)
				user_info = fdb.authe.get_account_info(idToken)

				# ['users']['localId']

				# Add data from BugLogForm to a dictionary
				data = {
					"Device": form.data.get("device"),
					"Feature": form.data.get("feature"),
					"Summary": form.data.get("summary"),
					"Steps": form.data.get("steps"),
					"Result": form.data.get("result")
				}
				form.save()
				print(data)
				# Add dictionary data to the database
				print("localid: " + user_info['users']['localId'])
				fdb.database.child("users").child(idToken).child("reports").child(millis).set(data)
				return HttpResponseRedirect('/home/', messages.error(request, message))
			except:
				message = "Something Error message"
				return redirect('/home/', messages.error(request, message))

			cd = form.cleaned_data
			# assert False
			return HttpResponseRedirect('/home?submitted=True')
	else:
		form = models.BugLogForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'home.html', {'form': form, 'submitted': submitted})
