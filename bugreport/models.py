from django.db import models

# Create your models here.
from accounts.models import CustomUser


class ReportFields(models.Model):
    DEVICE = 'device'
    FEATURE = "feature"
    SUMMARY = "summary"
    STEPS = "steps"
    RESULT = "result"


class Devices(models.Model):
    IPHONE6S = "6s"
    IPADMINI = "Mini"
    ANDROIDPIXEL = "Pixel"
    DEVICE_LIST = [
        (IPHONE6S, "Iphone 6s 20140928"),
        (IPADMINI, "Ipad Mini 20142706"),
        (ANDROIDPIXEL, "Google Pixel 20143536")
    ]


class Features(models.Model):
    THEIA = "Camera"
    TSTAT = "Tstat"
    SENSORS = "Sensors"
    LS = "Ls"
    ECO = "Eco_plus"
    IRIS = "Iris"
    FEATURE_LIST = [
        (THEIA, "Theia/Camera"),
        (TSTAT, "Thermostat"),
        (SENSORS, "Hecate/Rhodos"),
        (LS, "Light Switch"),
        (ECO, "Chronos/Eco+"),
        (IRIS, "Iris/Home monitoring/Invisible Guard")
    ]


class BugLogStructure(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    device = models.CharField(max_length = 50, choices = Devices.DEVICE_LIST,
                              default = Devices.DEVICE_LIST[0])
    feature = models.CharField(max_length = 50, choices = Features.FEATURE_LIST,
                               default = Features.FEATURE_LIST[0])
    summary = models.CharField(max_length = 100)
    steps = models.TextField(max_length = 350, default = "1. \n2.\n3.\n4.")
    result = models.TextField(max_length = 500, default = "Actual:\n\nExpected:\n")


class BashSessionInfo(models.Model):
    device = models.CharField(max_length = 50, choices = Devices.DEVICE_LIST,
                              default = Devices.DEVICE_LIST[0])
    feature = models.CharField(max_length = 50, choices = Features.FEATURE_LIST,
                               default = Features.FEATURE_LIST[0])
