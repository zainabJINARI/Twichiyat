from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


# Create your models here.


#Product Model :
class Product(models.Model) :

    product_type=models.CharField(max_length=200)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    size=models.CharField(max_length=5)
    color=models.CharField(max_length=15)
    description = models.TextField(max_length=500)
    image = models.ImageField(default='default.png' , blank=True)
    status = models.CharField(max_length=14 , default="Available")
    author = models.ForeignKey(User , null=True, on_delete=models.CASCADE)

    def _str_(self) :
        return self.product_type