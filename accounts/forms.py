from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        password = self.cleaned_data["password"]

        m = super().save(commit=False)

        if commit:
            m.set_password(password)
            m.save()

        return m


class UserLoginForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
