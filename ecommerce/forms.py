from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    name = forms.CharField(label = "Full Name", widget = forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label = "Email Address", widget = forms.EmailInput(attrs={"class": "form-control"}))
    content = forms.CharField(label = "Content", widget = forms.Textarea(attrs={"class": "form-control"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Error!, must use gmail")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username", widget = forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs={"class": "form-control"}))

class RegisterForm(forms.Form):
    username = forms.CharField(label = "Username", widget = forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.object.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Username already exists!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password:
            raise forms.ValidationError("Passwords Must Match")
        return data
