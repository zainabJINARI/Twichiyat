from django import forms
from .models import Product
from Store.models import Collection

class UpdateProduct(forms.ModelForm):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Ordered', 'Ordered'),
        ('Sold', 'Sold'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'style': 'overflow: auto;'}), initial='available')
   
    
    
    class Meta:
        model = Product
        fields = ['name', 'quantity','type_p', 'price', 'size', 'color', 'image', 'description', 'status']

    color_choices = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
        ('white', 'White'),
        ('Beige', 'Beige'),
        ('Magenta', 'magenta'),
        ('green', 'Green'),
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
        ('AS','All Sizes'),
        ('Stnd','Standard'),
    ]

    type_choices =[]
    for i in Collection.objects.all():
        print('am here')
        type_choices.append((str(i),str(i)))
    
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'style': 'overflow: auto;'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'overflow: auto;'}))
    color = forms.ChoiceField(choices=color_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))
    size = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))
    type_p = forms.ChoiceField(choices=type_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))

    # New fields
    


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity','type_p', 'price', 'size', 'color', 'image', 'description']

    color_choices = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
        ('white', 'White'),
        ('Beige', 'Beige'),
        ('Magenta', 'magenta'),
        ('green', 'Green'),
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
        ('AS','All Sizes'),
        ('Stnd','Standard')
    ]
    type_choices =[]
    for i in Collection.objects.all():
        type_choices.append((str(i),str(i)))
    print(type_choices)
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'style': 'overflow: auto;'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'overflow: auto;'}))
    color = forms.ChoiceField(choices=color_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))
    size = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))
    type_p = forms.ChoiceField(choices=type_choices, widget=forms.Select(attrs={'style': 'overflow: auto;'}))

    # New fields
    
