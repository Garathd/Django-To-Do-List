from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# USER'S PROFILE:
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile for all new users
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save() 