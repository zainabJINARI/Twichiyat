from django import forms
from .models import Order


class CreateOrder(forms.ModelForm):
    class Meta:
        model = Order  
        fields = ['name', 'address', 'city', 'phone_nbr' , 'postal_code']