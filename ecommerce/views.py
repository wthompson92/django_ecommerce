from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model


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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
            }
    print("User Logged In")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("Logging In")

        if user is not None:
            login(request, user)
            return redirect("/login")
        else:
            print("Error!")
    return render(request, "auth/login.html", context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
            }
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(email, password)

    return render(request, "auth/register.html", context)
