# Create your tests here.
from django.test import TestCase
from django.urls import reverse


class CreateReportTests(TestCase):
    def setUp(self) -> None:
        url = reverse('bugreport')
