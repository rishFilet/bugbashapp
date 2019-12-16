from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bugreport.forms import BugLogForm
from utils import clear_messages as clr


# Create your views here.
@login_required
def create_report(request):
    submitted = False
    clr.clear_msgs(request)
    if request.method == 'POST':
        form = BugLogForm(request.POST)
        if form.is_valid():
            try:
                message = "SUCCESS: Bug Report Submitted"
                bug = form.save(commit = False)
                bug.user = request.user
                bug.save()
                # Add dictionary data to the database
                return redirect(request.META['HTTP_REFERER'], messages.success(request,
                                                                               message))
            except:  # todo: refactor. Exception clause too broad
                message = "ERROR: Could not log bug successfully"
                return redirect('/bugreport/', messages.error(request, message))
    else:
        form = BugLogForm()

    return render(request, 'bugreport.html', {'form': form, 'submitted': submitted})
