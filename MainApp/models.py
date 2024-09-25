from django.db import models

# Create your models here.
class Color(models.Model):
   name = models.CharField(max_length=32)

   def __repr__(self):
       return self.name

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    item_description = models.TextField(max_length=1000, blank=True)
    colors = models.ManyToManyField(to=Color)






