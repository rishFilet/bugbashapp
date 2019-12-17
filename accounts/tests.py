# Create your tests here.
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.models import CustomUser
from accounts.views import register, login_view
from bugreport.views import  create_user_bug_view


class InvalidLoginTests(TestCase):
    def setUp(self) -> None:
        url = reverse('login_view')
        data = {
            'email': '',
            'password': ''
        }
        self.response = self.client.post(url, data)

    def test_login_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_redirect_to_login(self):
        view = resolve('/login/')
        self.assertEquals(view.func, login_view)


class ValidLoginTests(TestCase):
    def setUp(self) -> None:
        username = 'test@test.com'
        password = 'Test3Test#'
        CustomUser.objects.create_user(email=username, password=password)
        self.user = self.client.login(email=username, password=password)
        self.bug_report_url = reverse('bug_report')

    def test_redirect_to_bug_report_page(self):
        view = resolve('/bugreport/')
        self.assertEquals(view.func, create_user_bug_view)


class RegisterTest(TestCase):
    def setUp(self):
        self.url = reverse('register')
        data = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'password1': 'Test3Test#',
            'password2': 'Test3Test#'
        }
        self.response = self.client.post(self.url, data)
        self.bug_home_url = reverse('home')

    def test_signup_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_register_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func, register)

    def test_create_account_resolves_to_bugreport_page(self):
        self.assertRedirects(self.response, self.bug_home_url)
