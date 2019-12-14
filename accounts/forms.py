from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password', 'role')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any account already exist with this email as a username.
        try:
            CustomUser.objects.get(email=email)
        except:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'role',)
