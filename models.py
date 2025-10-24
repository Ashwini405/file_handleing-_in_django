from django.db import models

# Create your models here.
class userReg(models.Model):
    name=models.CharField( max_length=30,null=False)
    email=models.EmailField(max_length=100,default="user@gmail.com")
    mobile=models.CharField(max_length=10,unique=True,primary_key=True)
    pic=models.FileField(upload_to="profile",null=True, blank=True)
 