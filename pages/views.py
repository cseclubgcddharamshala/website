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
   
    all_notices = [
        {'title': 'Mid-Term Exam Schedule', 'date': 'Feb 20, 2026', 'priority': 'High'},
        {'title': 'Coding Club Meeting', 'date': 'Feb 22, 2026', 'priority': 'Medium'},
    ]
    return render(request, 'pages/notices.html', {'notices': all_notices})