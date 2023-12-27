from django.db import models

# Create your models here.
class Product(models.Model) :
      type_p = models.CharField(max_length=25)
      price = models.IntegerField()
      size = models.CharField(max_length=4)
      color = models.CharField(max_length=25)
      description = models.TextField(max_length=400)
      image = models.ImageField(default='default.png' , blank=True)

        
class Collection(models.Model):
    name = models.CharField(max_length=25)
    image_col= models.ImageField(default='default.png',blank=True)
    slugC =  models.SlugField(max_length=50,default=None)
    def __str__(self):
        return self.name
    