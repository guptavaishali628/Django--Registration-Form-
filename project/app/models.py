from django.db import models

# Create your models here.

# inherite model from models
# mandatory to define max_length 
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.IntegerField(max_length=50)
    Details=models.CharField(max_length=50)
    #  install pillow from python lib for image store
    Image=models.ImageField(upload_to='image/')
    
    # this method used for string type data print on the html page data.html
    def __str__(self):
        return self.Name +" "+ self.Email
    
    # this method used for int type data print on the html page data.html by doing typecasting
    # def __str__(self):
    #     return str(self.Contact)
    