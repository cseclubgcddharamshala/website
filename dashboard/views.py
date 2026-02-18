from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    """
    Renders the student dashboard.
    Only accessible if the user is logged in.
    """
    # You can fetch extra data here later (like joined clubs, events, etc.)
    context = {
        'student': request.user,
        'message': 'Welcome to your student portal!'
    }
    return render(request, 'dashboard/index.html', context)