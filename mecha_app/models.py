import email
from select import select
from django.db import models

# Create your models here.
class userForm (models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    select =models.CharField(max_length=100)
    message = models.TextField(max_length= 1000, default= "my service")
    
    def __str__(self):
        return self.name 

   