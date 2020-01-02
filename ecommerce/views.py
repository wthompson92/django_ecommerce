from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import ContactForm

def home(request):
    context = {
        "title": "Home Page"
        }
    return render(request, "home.html", context)

def about(request):
    context = {
        "title": "About Page"
    }
    return render(request, "home.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "Contact",
        "form": contact_form
    }
    #
    if contact_form.is_valid():
        print(contact_form.cleaned_data)


    return render(request, "contact/view.html", context)
