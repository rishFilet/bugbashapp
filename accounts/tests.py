# Create your tests here.
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.views import register


class LoginTests(TestCase):
    pass
    # def test_login_blank_fields(self):
    #     url = reverse('login_view')
    #     response = self.client.post(url, ())
    #     form = response.context.get('form')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTrue(form.errors)


class RegisterTest(TestCase):
    def setUp(self):
        url = reverse('register')
        data = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'password1': 'Test3Test#',
            'password2': 'Test3Test#'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_signup_status_code(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_register_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func, register)

    def test_create_account_resolves_to_home_page(self):
        self.assertRedirects(self.response, self.home_url)
