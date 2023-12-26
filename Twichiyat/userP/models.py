from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Women = 'Women'
    Men = 'Men'
    GENDER_CHOICES = (
        (Women, 'Women'),
        (Men, 'Men')
    )
    
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)
    address = models.CharField(max_length=150)
    phone_nbr = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default=Women)
    slugU =  models.SlugField(max_length=50,default=None)

    def __str__(self):
        return self.user.username
