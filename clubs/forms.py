from django import forms
from .model import Project 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # FIXED: Changed 'github_link' to 'project_link' to match your model exactly
        fields = ['title', 'description', 'project_link'] 
        
        # Updated the widgets to match the correct field name
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Nexus-Campus Portal'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'project_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'})
        }