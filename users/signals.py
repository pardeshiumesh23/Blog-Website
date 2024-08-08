#This file is for or logic is that when the user register/sign up then automatically the profile will be created and
# you don't need go back to the backend and manually change the profile. We use singals for this

from django.contrib.auth.models import User
from .models import ProfileModel
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profilr(sender,instance, created,*args, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)      