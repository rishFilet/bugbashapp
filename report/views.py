from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def showReport(request):
    submitted = False
    if request.method == 'POST':
        form = models.BugLogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/home?submitted=True')
    else:
        form = models.BugLogForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home.html', {'form': form, 'submitted': submitted})
