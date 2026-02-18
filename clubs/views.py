from django.shortcuts import render, get_object_or_404
from .model import Club

def club_list(request):
    """
    Fetches all clubs from the database.
    """
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})

def club_detail(request, club_slug):
    """
    Fetches a single club.
    If the club_type is 'tech', it loads a special coding template.
    Otherwise, it loads the standard club template.
    """
    club = get_object_or_404(Club, slug=club_slug)
    
    # Logic to choose the right template based on club type
    if club.club_type == 'tech':
        template_name = 'clubs/detail_coding.html'
    elif club.club_type == 'sports':
        template_name = 'clubs/detail_sports.html'
    else:
        template_name = 'clubs/detail_generic.html'

    return render(request, template_name, {'club': club})