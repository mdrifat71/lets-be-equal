from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class RecieverLocation(models.Model):
    country = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    lat = models.DecimalField(max_digits = 9, decimal_places = 6, null = True, db_index=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null= True, db_index=True)


class Campaign(models.Model):
    owner = models.ForeignKey(to=User, on_delete = models.CASCADE, related_name='campaign_owner')
    title = models.CharField(max_length = 200)
    slug = models.CharField(unique = True, max_length=500)
    target_ammount = models.DecimalField(max_digits=15, decimal_places=6)
    raised_ammount = models.DecimalField(max_digits=15, decimal_places=6, default=0)
    location = models.ForeignKey(to=RecieverLocation, on_delete= models.CASCADE, related_name='campaign_location', null=True, blank = True)
    prioriy = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class CampaignImage(models.Model):
    campaign = models.ForeignKey(to = Campaign, on_delete= models.CASCADE, related_name='imageTocampaign')
    image = models.ImageField(null = True, blank = True)

class Comment(models.Model):
    owner = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name='comment_owner')
    host = models.ForeignKey(to = Campaign, on_delete= models.CASCADE, related_name='comment_to_campaign')
    body = models.TextField(max_length= 2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

