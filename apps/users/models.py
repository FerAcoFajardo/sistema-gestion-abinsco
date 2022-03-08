from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randrange

def random_image_chooser():
    """This defines the default image for the user"""
    images = [
        'profiles/generic/profile_happy.png',
        'profiles/generic/profile_kakashi.jpg',
        'profiles/generic/profile_whats.jpg',
    ]
    i = randrange(3)
    return images[i]

class User(AbstractUser):
    image = models.ImageField(upload_to='profiles/', max_length=255, blank=True, null=True, default=random_image_chooser())
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    dark_mode = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']