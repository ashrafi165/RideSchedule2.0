from django.db import models
from django.contrib.auth.models import User
import json


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    rate = models.FloatField(null=True,blank=True)
    rateCount = models.IntegerField(blank=True,null=True)
    serviceCount = models.IntegerField(blank=True,null=True)
    birthday = models.DateField(null= True,blank=True)
    history = models.TextField(null =True, blank= True)

    isRider = models.BooleanField(default=False)

    image = models.ImageField(upload_to='upload', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def get_history(self):
        return json.loads(self.history) if self.history else []

    def set_history(self, history_list):
        self.history = json.dumps(history_list)
  

class Rate(models.Model):
    user_id = models.CharField(blank=True,null=True,max_length=20)
    rate =  models.FloatField(null=True,blank=True)

    
    def __str__(self):
        return self.user_id

class Notification(models.Model):
    user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(blank=True,null=True,max_length=20)
    message = models.CharField(blank=True,null=True,max_length=50)
    
