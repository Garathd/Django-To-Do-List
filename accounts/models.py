from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Create a user profile model
"""
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to="img/user", blank=True, null=True)
    account = models.CharField(max_length=40, default='free')
    
    
"""
Create a user profile for all new users
"""
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save() 