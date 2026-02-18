from django.urls import path
from . import views

urlpatterns = [
    # Path: www.yourwebsite.com/
    path('', views.home, name='home'),

    # Path: www.yourwebsite.com/about/
    path('about/', views.about, name='about'),

    # Path: www.yourwebsite.com/contact/
    path('contact/', views.contact, name='contact'),
    path('notices/', views.notices, name='notices'),
]