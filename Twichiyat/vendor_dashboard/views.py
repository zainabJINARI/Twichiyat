from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 
from userP.models import Profile
from userP.forms import UserUpdateForm, ProfileUpdateForm
from . import forms
from .models import Product

# Create your views here.
@login_required( login_url="/userP/login")
def dashboard_home(request):
    return render(request,'vendor_dashboard/dashboard.html')

@login_required(login_url="/userP/login")
def update_account(request):
    try:
        current_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        current_profile = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=current_profile.user)
        profile_form = ProfileUpdateForm(request.POST, instance=current_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            #user.save()
            user=user_form.save()
            current_profile.address = profile_form.cleaned_data['address']
            current_profile.phone_nbr = profile_form.cleaned_data['phone_nbr']
            current_profile.gender = profile_form.cleaned_data['gender']
            current_profile.slugU = profile_form.cleaned_data['slugU']
            current_profile.save()
            if current_profile:
                profile_form.save()
            login(request, user)
            return redirect('vendor_dashboard:dashboard')
    else:
        user_form = UserUpdateForm(instance=current_profile.user)
        profile_form = ProfileUpdateForm(instance=current_profile)

    return render(request, 'vendor_dashboard/update_account.html', {'user_form': user_form, 'profile_form': profile_form, 'currentProfile': current_profile})
@login_required(login_url="/userP/login")
def delete_account(request):
    if request.method=='POST':
        current_profile = Profile.objects.get(user=request.user)
        current_profile.user.delete()
        return redirect('home')
    
def product_area(request) :
    products = Product.objects.all() 
    return render(request , 'vendor_dashboard/product_area.html',{'products' :products})


def add_product(request) :
    if request.method == 'POST' :
        form = forms.CreateProduct(request.POST , request.FILES)
        if form.is_valid() :
            instance = form.save(commit=False)
            instance.author =request.user 
            instance.save()
            return redirect('vendor_dashboard:product_area')
    
    else :
        form = forms.CreateProduct()
    return render(request , 'vendor_dashboard/add_product.html' , {'form':form })
    
