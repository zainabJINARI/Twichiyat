from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=25,default='Anonymous Product')
    type_p = models.CharField(max_length=25)
    price = models.IntegerField()
    size = models.CharField(max_length=4)
    color = models.CharField(max_length=25)
    description = models.TextField(max_length=400)
    image = models.ImageField(default='default.png', blank=True)
    date = models.DateTimeField(default=datetime.datetime.now, editable=False)
    quantity = models.IntegerField(default=1)
    author = models.ForeignKey(User , null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=14 , default="Available")
    def save(self, *args, **kwargs):
        # Set default value for date if not provided
        if not self.date:
            self.date = datetime.datetime.now()
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name