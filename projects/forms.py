from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        
        model = Project
        fields = ('name', 'description', 'status')
        labels = {
            'name': 'Please enter a project name',
            'description': 'Please enter a project description'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }
