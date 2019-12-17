# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from bugreport.models import BugLogStructure, ReportFields, BashSessionInfo


class BugLogForm(forms.ModelForm):
    class Meta:
        model = BugLogStructure
        fields = [
            ReportFields.DEVICE,
            ReportFields.FEATURE,
            ReportFields.SUMMARY,
            ReportFields.STEPS,
            ReportFields.RESULT
        ]
        widgets = {
            'summary': forms.TextInput(attrs={
                'required': True,
                'placeholder': 'Enter Summary...'
            }),
            'steps': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Enter Descriptive Steps To Reproduce issue'
            }),
            'result': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Enter Expected and Actual Result'
            }),
        }

class BashSessionForm(forms.ModelForm):
	class Meta:
		model = BashSessionInfo
		fields = [
			ReportFields.FEATURE,
			ReportFields.DEVICE
		]
