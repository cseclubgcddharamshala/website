from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clubs.model import Project  

@login_required
def dashboard(request):
    """
    Renders the student dashboard.
    Fetches the logged-in user's projects from the database.
    """
    # 1. Ask the database for this specific student's projects
    my_projects = Project.objects.filter(student=request.user).order_by('-created_at')
    
    # 2. Package those projects up to send to the HTML file
    context = {
        'user': request.user,
        'my_projects': my_projects,
        'message': 'Welcome to your student portal!'
    }
    
    # 3. Send it to the template!
    return render(request, 'dashboard/index.html', context)