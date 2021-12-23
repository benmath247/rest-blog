from django import forms

from accounts.models import User

class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
