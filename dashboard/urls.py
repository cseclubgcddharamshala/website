from django.urls import path
from . import views

# Ensure this variable name is spelled correctly and is a list []
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]