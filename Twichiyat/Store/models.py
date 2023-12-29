from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User


        
class Collection(models.Model):
    name = models.CharField(max_length=25)
    image_col= models.ImageField(default='default.png',blank=True)
    slugC =  models.SlugField(max_length=50,default=None)
    def __str__(self):
        return self.name
    