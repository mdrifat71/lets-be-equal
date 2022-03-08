from django.db import models
from django.contrib.auth.models import User

class UserLocation(models.Model):
    country = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    lat = models.DecimalField(max_digits = 9, decimal_places = 6, null = True, db_index=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null= True, db_index=True)

class UserProfile(models.Model):
    owner = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name='profile_owner')
    location = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name='user_location')
    image = models.ImageField(null = True, blank = True)
