# apic/rails/forms.py
from django import forms


class AuthenticateForm(forms.Form):
    email = forms.EmailField(max_length=256, label="Username")
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
