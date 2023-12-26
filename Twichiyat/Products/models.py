from django.db import models

# Create your models here.

class Product(models.Model) :
      type_p = models.CharField(max_length=25)
      price = models.IntegerField()
      size = models.CharField(max_length=4)
      color = models.CharField(max_length=25)
      description = models.TextField(max_length=400)
      image = models.ImageField(default='default.png' , blank=True)
      #owner 
      #Reviews 

      def __str__(self) :
            return  "Type :{0} , Price:{1}".format(self.type_p , self.price)




