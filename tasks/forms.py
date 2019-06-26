from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'priority', 'screenshot')
        labels = {
            'name': 'Please enter a task name',
            'description': 'Please enter a task description'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'screenshot': forms.ClearableFileInput(attrs={
                'class':'btn btn-default auto-width'
            }),
        }
  