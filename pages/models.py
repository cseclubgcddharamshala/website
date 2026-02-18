from django.db import models

class Notice(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High Priority'),
        ('Medium', 'Medium Priority'),
        ('Low', 'Low Priority'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Detailed description of the notice.")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    external_link = models.URLField(blank=True, null=True, help_text="Link to a PDF, Google Form, or external site.")
    embed_code = models.TextField(blank=True, null=True, help_text="Paste the full iframe embed code here (e.g., from YouTube or Google Forms).")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title