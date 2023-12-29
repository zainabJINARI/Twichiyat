from django import forms 
from . import models
from django import forms
from .models import Product

class UpdateProduct(forms.ModelForm):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Ordered', 'Ordered'),
        ('Sold', 'Sold'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'style': 'overflow: auto;'}), initial='available')

    class Meta:
        model = Product
        fields = ['product_type', 'price', 'size', 'color', 'image', 'description', 'status']

    color_choices = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        # Add more choices as needed
    ]
    size_choices = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('3XL', 'Triple Extra Large'),
    ]
    type_choices = [
        ('dress', 'Dress'),
        ('jacket', 'Jacket'),
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        # Add more choices as needed
    ]

    color = forms.ChoiceField(choices=color_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))
    size = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))
    product_type = forms.ChoiceField(choices=type_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))



class CreateProduct(forms.ModelForm) :
    class Meta :
        model = models.Product 
        fields =['product_type' , 'price' , 'size' , 'color' , 'image' , 'description']  
    color_choices = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        # Ajoutez d'autres choix au besoin
    ]
    size_choices = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('3XL', 'Triple Extra Large'),
    ]
    type_choices = [
        ('dress', 'Dress'),
        ('jacket', 'Jacket'),
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        # Add more choices as needed
    ]

    color = forms.ChoiceField(choices=color_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))  
    size = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'})) 
    product_type = forms.ChoiceField(choices=type_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))