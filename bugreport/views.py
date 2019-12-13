from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import models


# Create your views here.
@login_required
def create_report(request):
    submitted = False
    if request.method == 'POST':
        form = models.BugLogForm(request.POST)
        if form.is_valid():
            try:
                message = "SUCCESS: Bug Report Submitted"
                form.save()
                # Add dictionary data to the database
                return HttpResponseRedirect('/home/', messages.error(request, message))
            except:
                message = "ERROR: Could not log bug successfully"
                return redirect('/home/', messages.error(request, message))
    else:
        form = models.BugLogForm()

    return render(request, 'bugreport.html', {'form': form, 'submitted': submitted})
