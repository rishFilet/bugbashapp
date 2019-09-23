from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


class BugLogForm(forms.Form):
    yourName = forms.CharField(max_length = 100, label = 'Your Name')
    email = forms.EmailField(required = False, label = 'Your e-mail address')
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = BugLogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/home?submitted=True')
    else:
        form = BugLogForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home.html', {'form': form, 'submitted': submitted})
