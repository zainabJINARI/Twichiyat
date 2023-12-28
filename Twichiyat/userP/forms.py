from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile  # Import your Profile model
from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data



class CreateUser(UserCreationForm):

    address = forms.CharField()
    phone_nbr = forms.CharField()
    gender = forms.CharField()
    slugU =  forms.SlugField()
    
    class Meta:
        model = User
        fields =['username','email','password1','password2','address','phone_nbr','slugU','gender']
        
        




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_nbr', 'gender', 'slugU']
