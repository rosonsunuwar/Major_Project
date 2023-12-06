from django.db import models

# Create your models here.
class Saree(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='saree/')
    
    def __str__(self):
        return self.name
    
class Kurtha(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='kurtha/')
    
    def __str__(self):
        return self.name
class T_Shirt(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='t-shirt/')
    
    def __str__(self):
        return self.name

class Pant(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='pant/')
    
    def __str__(self):
        return self.name



