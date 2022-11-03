
from distutils.command.upload import upload
from django.db import models

# Create your models here.
   
    
class needblood(models.Model):
    Name = models.CharField(max_length=100)
    Mobile=models.BigIntegerField(default=0)
    Type= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    Area= models.CharField(max_length=100)
    City= models.CharField(max_length=100)
    
class donate(models.Model):
    Name = models.CharField(max_length=100)
    Mobile=models.BigIntegerField(default=0)
    Type= models.CharField(max_length=100)
    Area= models.CharField(max_length=100)
    City= models.CharField(max_length=100)
    
    
    
    
    
