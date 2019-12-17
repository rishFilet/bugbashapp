import json

from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from bugreport.forms import BugLogForm, BashSessionForm
from leaderboard.views import update_lb
from utils import clear_messages as clr


# Create your views here.
from bugreport.models import BugLogStructure


@login_required
def create_user_bug_view(request):
    clr.clear_msgs(request)
    template_vars = {
        'all_bugs': BugLogStructure.objects.reverse(),
        'form': BugLogForm(
            initial = {'device': request.session['device'], 'feature': request.session['feature']})
    }
    return render(request, 'bugreport.html', template_vars)


@login_required
def create_report(request):
    clr.clear_msgs(request)
    if request.method == 'POST':
        try:
            logged_bug = BugLogStructure(
                user=request.user,
                device=request.POST.get('device'),
                feature=request.POST.get('feature'),
                summary=request.POST.get('summary'),
                steps=request.POST.get('steps'),
                result=request.POST.get('result'))
            logged_bug.save()
            response_data = {
                'summary': request.POST.get('summary')
            }
            return JsonResponse(response_data)
        except IntegrityError:
            raise
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



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
