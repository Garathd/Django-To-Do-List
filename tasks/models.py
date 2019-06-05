from django.db import models
from django.utils import timezone
from projects.models import Project
from django.contrib.auth.models import User

status = [
    ('To Do','To Do'),
    ('In Progress','In Progress'),
    ('Done','Done'),
]

priority = [
    ('Low','Low'),
    ('Medium','Medium'),
    ('High','High'),
    ]

# Create your models here.
class Task(models.Model):

    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=255, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False, null=True)
    status = models.CharField(max_length=40, choices=status, default='To Do')
    priority = models.CharField(max_length=40, choices=priority, default='Low')
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.name