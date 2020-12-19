from django.db import models

# Create your models here.
class email(models.Model):
    Email=models.EmailField()
    password= models.IntegerField()
