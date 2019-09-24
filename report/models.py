from django.db import models
from django.forms import ModelForm
from enum import Enum


# Create your models here.
class fields(models.Model):
    DEVICE = 'device'
    FEATURE = "feature"
    SUMMARY = "summary"
    STEPS = "steps"
    RESULT = "result"

class Devices(models.Model):
    IPHONE6S = "6s"
    IPADMINI = "Mini"
    DEVICE_LIST = [
        (IPHONE6S, "Iphone 6s 20140928"),
        (IPADMINI, "Ipad Mini 20142706")
    ]

class Features(models.Model):
    THEIA = "Camera"
    TSTAT_REG = "Tstat Reg"
    FEATURE_LIST = [
        (THEIA, "Theia/Camera"),
        (TSTAT_REG, "Tstat Registration")
    ]

class BugLogStructure(models.Model):
    device = models.CharField(max_length = len(Devices.DEVICE_LIST), choices =
    Devices.DEVICE_LIST, default=Devices.DEVICE_LIST[0])
    feature = models.CharField(max_length = len(Features.FEATURE_LIST), choices =
    Features.FEATURE_LIST, default = Features.FEATURE_LIST[0])
    summary = models.CharField(max_length = 100)
    steps = models.CharField(max_length = 100)
    result = models.TextField(max_length = 500, default="Enter a descriptive result here")


class BugLogForm(ModelForm):
    class Meta:
        model = BugLogStructure
        fields = [fields.DEVICE, fields.FEATURE, fields.SUMMARY, fields.STEPS,fields.RESULT]