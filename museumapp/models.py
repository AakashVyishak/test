from django.db import models

# Create your models here.
class item(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    im=models.ImageField(upload_to='picture')
    offer=models.BooleanField(default=False)
class books(models.Model):
    name=models.CharField(max_length=100)
    price = models.IntegerField()
    im = models.ImageField(upload_to='picture')