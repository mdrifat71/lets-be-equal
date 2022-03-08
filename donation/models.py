from django.db import models
from django.contrib.auth.models import User
from campaign.models import Campaign



class Donation(models.Model):
    donner = models.ForeignKey(to = User, on_delete = models.SET_NULL, null = True, related_name= 'donner')
    campaign = models.ForeignKey(to = Campaign, on_delete= models.SET_NULL, null = True, related_name='reciever_campaign')
    receiver = models.ForeignKey(to = User, on_delete= models.SET_NULL, related_name= 'donation_reciever', null = True)
    ammount = models.IntegerField()
    donner_name = models.CharField(max_length= 200)
    donner_email = models.EmailField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

