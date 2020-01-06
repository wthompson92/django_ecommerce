from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
]
