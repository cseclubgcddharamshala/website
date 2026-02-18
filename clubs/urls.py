from django.urls import path
from . import views

urlpatterns = [
    # Path: www.yourwebsite.com/clubs/
    # Shows the list of all clubs
    path('', views.club_list, name='club_list'),

    # Path: www.yourwebsite.com/clubs/coding-club/
    # The <slug> part captures the club name from the URL
    path('<slug:club_slug>/', views.club_detail, name='club_detail'),
]