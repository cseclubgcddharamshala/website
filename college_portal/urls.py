from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Make sure this line exists to connect your clubs URLs!
    path('clubs/', include('clubs.urls')), 
    
    path('dashboard/', include('dashboard.urls')),
    # ... any other apps ...
]