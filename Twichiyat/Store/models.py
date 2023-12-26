from django.db import models

# Create your models here.
class Product(models.Model) :
      type_p = models.CharField(max_length=25)
      price = models.IntegerField()
      size = models.CharField(max_length=4)
      color = models.CharField(max_length=25)
      description = models.TextField(max_length=400)
      image = models.ImageField(default='default.png' , blank=True)
      slugP =  models.SlugField(max_length=50,default=None)
      #owner 
      #Reviews 
      #Status

      def __str__(self) :
            return  "Type :{0} , Price:{1}".format(self.type_p , self.price)
        
class Collection(models.Model):
    name = models.CharField(max_length=25)
    image_col= models.ImageField(default='default.png',blank=True)
    slugC =  models.SlugField(max_length=50,default=None)
    def __str__(self):
        return self.name
    