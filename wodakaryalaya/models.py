from django.db import models

# Create your models here.
class Birth(models.Model):
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
 
    desc = models.TextField()
 
