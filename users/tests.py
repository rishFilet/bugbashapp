# Create your tests here.
from django.test import TestCase
from django.urls import reverse, resolve

from users.views import register


class LoginTests(TestCase):
    pass
    # def test_login_blank_fields(self):
    #     url = reverse('login_view')
    #     response = self.client.post(url, ())
    #     form = response.context.get('form')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTrue(form.errors)


class RegisterTest(TestCase):
    def test_signup_status_code(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_register_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func, register)
