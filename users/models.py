from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator #this is used for validating file types and extensions 
                                                          #means what user can upload ex. img,video,file etc we have t0 specify below
# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile',validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self) -> str:
        return self.user.username   