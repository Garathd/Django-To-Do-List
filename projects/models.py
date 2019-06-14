from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    
    status = (
        ('Work','Work'),
        ('Education', 'Education'),
        ('Personal','Personal'),
    )

    
    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=40, choices=status, default='Work')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.name
 