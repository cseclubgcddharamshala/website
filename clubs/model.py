from django.db import models
from django.utils.text import slugify

class Club(models.Model):
    CLUB_TYPES = (
        ('tech', 'Technical & Coding'),
        ('cultural', 'Art & Culture'),
        ('sports', 'Sports & Fitness'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True) # e.g., 'coding-club'
    club_type = models.CharField(max_length=20, choices=CLUB_TYPES, default='tech')
    description = models.TextField()
    logo = models.ImageField(upload_to='club_logos/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Auto-generate the URL slug if empty
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.club.name}"