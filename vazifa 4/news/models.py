from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50,unique=True)
    country = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name
    
    
class Car(models.Model):
    name = models.CharField(max_length=50,unique=True)
    price = models.IntegerField()
    year = models.IntegerField()
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='Car/photos/',blank=True,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name