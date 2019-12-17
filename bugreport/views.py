from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bugreport.forms import BugLogForm, BashSessionForm
from leaderboard.views import update_lb
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
                update_lb(request)
                # Add dictionary data to the database
                return redirect(request.META['HTTP_REFERER'], messages.success(request,
                                                                               message))
            except:  # todo: refactor. Exception clause too broad
                message = "ERROR: Could not log bug"
                return redirect('/bugreport/', messages.error(request, message))
    else:
        form = BugLogForm(
            initial = {'device': request.session['device'], 'feature': request.session['feature']})
    return render(request, 'bugreport.html', {'form': form, 'submitted': submitted})


@login_required
def create_bashing_session(request):
    submitted = False
    if request.method == "POST":
        form = BashSessionForm(request.POST)
        if form.is_valid():
            try:
                message = "Starting Bash Session!"
                request.session['feature'] = request.POST['feature']
                request.session['device'] = request.POST['device']
                bash_session = form.save(commit = False)
                bash_session.user = request.user
                bash_session.save()

                return redirect('/bugreport/', messages.success(request, message))

            except:
                message = "ERROR: Could not Start Bash Session successfully"
                return redirect('/home', messages.error(request, message))
    else:
        form = BashSessionForm()

    return render(request, 'startpage.html', {'form': form, 'submitted': submitted})
