from django.db import models

# Create your models here.
class Productmodel(models.Model):
    Product_Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile_no=models.IntegerField()
