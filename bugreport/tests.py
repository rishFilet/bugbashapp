# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser


class CreateReportTests(TestCase):
    def setUp(self) -> None:
        username = 'test@test.com'
        password = 'Test3Test#'
        CustomUser.objects.create_user(email=username, password=password)
        self.url = reverse('bug_report')
        data = {
            "device": "camera",
            "feature": "Iphone 6s 20140928",
            "summary": "Test Summary",
            "steps": "Test Steps",
            "result": "Test Result"
        }
        self.client.login(email=username, password=password)
        self.response = self.client.post(self.url, data)
        self.bug_report_url = reverse('bug_report')

    def test_bug_submit_success_code(self):
        self.assertEquals(self.response.status_code, 302)

    def test_bug_submit_redirect(self):
        login_url = reverse('login_view')
        self.assertRedirects(self.response, f'{login_url}?next={self.bug_report_url}')
