from django.db import models

# Create your models here.

# inherite model from models
# mandatory to define max_length 
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    Contact=models.IntegerField(max_length=50)
    details=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/')
    #  install pillow from python lib for image store
    