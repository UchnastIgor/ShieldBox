from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

def upload_to(inst, filename):
    return "/profile/"+ str(filename)

class User(AbstractUser):
    # email = models.EmailField(max_length = 55, unique=True)
    username = models.CharField(max_length = 55, unique=False) 
    nicname = models.CharField(max_length = 55, default='default_nicname')
    profile_picture = ResizedImageField(upload_to = "", null = True, blank = True)

