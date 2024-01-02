from django.contrib import admin

# Register your models here.
from .models import Collection
from .models import Order,OrderItem


admin.site.register(Collection)
admin.site.register(Order)
admin.site.register(OrderItem)


