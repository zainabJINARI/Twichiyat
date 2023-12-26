from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import models
from django.contrib.auth.models import User
class CreateUser(UserCreationForm):

    address = forms.CharField()
    phone_nbr = forms.CharField()
    gender = forms.CharField()
    slugU =  forms.SlugField()
    class Meta:
        model = User
        fields =['username','email','password1','password2','address','phone_nbr','slugU','gender']