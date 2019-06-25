from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'priority', 'screenshot')
        labels = {
            'name': 'Please enter a project name',
            'description': 'Please enter a project description'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }
  