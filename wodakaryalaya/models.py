from django.db import models

# Create your models here.
class Birth(models.Model):
    genders=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    birthday=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    marriageId=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    provience=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=genders)
 
   
 
