from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from vendor_dashboard.models import Product

        
class Collection(models.Model):
    name = models.CharField(max_length=25)
    image_col= models.ImageField(default='default.png',blank=True)
    slugC =  models.SlugField(max_length=50,default=None)
    def __str__(self):
        return self.name
    


    
    
class Order(models.Model) : 
     
   name=models.CharField(max_length = 25)  
   address = models.CharField(max_length=200)
   city = models.CharField(max_length=20)
   phone_nbr = models.CharField(max_length=30)
   postal_code = models.CharField(max_length=10 ,default='00000')
   note=models.CharField(max_length = 25,default='No comment ')
   date = models.DateTimeField(default=datetime.datetime.now, editable=False)
   products = models.ManyToManyField(Product, through='OrderItem')
   
   
   def save(self, *args, **kwargs):
        # Set default value for date if not provided
        if not self.date:
            self.date = datetime.datetime.now()
        super(Order, self).save(*args, **kwargs)
   
   def _str_(self) :
       return self.name
   
   
class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Assuming quantity cannot be negative