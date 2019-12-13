from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
                #  todo : refactor to bug report page
                return redirect(request.META['HTTP_REFERER'], messages.success(request,
                                                                               message))
            except:  # todo: refactor. Exception clause too broad
                message = "ERROR: Could not log bug successfully"
                #  todo : refactor to bug report page
                return redirect('/bugreport/', messages.error(request, message))
    else:
        form = models.BugLogForm()

    return render(request, 'bugreport.html', {'form': form, 'submitted': submitted})
