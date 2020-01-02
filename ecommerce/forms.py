from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Full Name", widget = forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label = "Email Address", widget = forms.EmailInput(attrs={"class": "form-control"}))
    content = forms.CharField(label = "Content", widget = forms.Textarea(attrs={"class": "form-control"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Error!, must use gmail")
        return email
