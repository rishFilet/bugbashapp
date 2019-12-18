import json

from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from bugreport.forms import BugLogForm, BashSessionForm
from utils import clear_messages as clr
from bugreport.models import BugLogStructure
from utils import clear_messages as clr
from utils.bug_bash_switch import switch as sw


@login_required
def create_user_bug_view(request):
    clr.clear_msgs(request)
    template_vars = {
        'all_bugs': BugLogStructure.objects.filter(user=request.user).reverse(),
        'form': BugLogForm(
            initial={'device': request.session['device'], 'feature': request.session['feature']})
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
                'id': logged_bug.id,
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
    clr.clear_msgs(request)
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
    messages.info(request, sw().status())
    return render(request, 'startpage.html', {'form': form, 'submitted': submitted})


@login_required
def update_bug(request):
    print("Test")
    if request.method == "POST":
        id1 = request.POST.get('id', None)
        new_summary = request.POST.get('summary', None)
        new_steps = request.POST.get('steps', None)
        new_result = request.POST.get('result', None)

        obj = BugLogStructure.objects.filter(user=request.user).get(id=id1)
        obj.summary = new_summary
        obj.steps = new_steps
        obj.result = new_result
        obj.save()

        data = {
            'id': obj.id,
            'summary': obj.summary,
        }
        return JsonResponse(data)
