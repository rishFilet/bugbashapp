# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from bugreport.models import BugLogStructure, ReportFields


class BugLogForm(ModelForm):
    class Meta:
        model = BugLogStructure
        fields = [
            ReportFields.DEVICE,
            ReportFields.FEATURE,
            ReportFields.SUMMARY,
            ReportFields.STEPS,
            ReportFields.RESULT
        ]
