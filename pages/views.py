from sys import path
from django.shortcuts import render

from dashboard import views

def home(request):
    """
    Renders the main homepage.
    Expected Template: templates/home.html
    """
    return render(request, 'home.html')

def about(request):
    """
    Renders the about page (Arshita's section).
    Expected Template: templates/pages/about.html
    """
    return render(request, 'pages/about.html')

def contact(request):
    """
    Renders the contact page (Divyanshi's section).
    Expected Template: templates/pages/contact.html
    """
    return render(request, 'pages/contact.html')

def notices(request):
    """
    Renders the central notice board.
    """
    from .models import Notice
    notices = Notice.objects.filter(is_active=True).order_by('-created_at')
    
    return render(request, 'pages/notices.html', {'notices': notices})