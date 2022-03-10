from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from campaign.models import Campaign



class Donation(models.Model):
    donner = models.ForeignKey(to = User, on_delete = models.SET_NULL, null = True, related_name= 'donner')
    campaign = models.ForeignKey(to = Campaign, on_delete= models.SET_NULL, null = True, related_name='reciever_campaign')
    ammount = models.IntegerField()
    donner_name = models.CharField(max_length= 200)
    donner_email = models.EmailField()
    audit = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

