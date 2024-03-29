from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 
from userP.models import Profile
from userP.forms import UserUpdateForm, ProfileUpdateForm
from . import forms
from .models import Product
from django.http import HttpResponse, JsonResponse
from .forms import UpdateProduct
from django.shortcuts import get_object_or_404
from django.db.models import Q
from itertools import groupby
from operator import attrgetter
from Store.models import Order,OrderItem
import re

# Create your views here.
@login_required( login_url="/userP/login")
def dashboard_home(request):
    current_profile = Profile.objects.get(user=request.user)
    if current_profile.is_vendor == True:
        productsVendor = Product.objects.filter(author=request.user)
        itemsOrder = OrderItem.objects.filter(product__in=productsVendor)
        
        grouped_items = {}

        for key, group in groupby(itemsOrder, key=attrgetter('order')):
            order_items = list(group)
            total_price=0
            for item in order_items:
                total_price += item.product.price * item.quantity
                
            if key not in grouped_items:
                grouped_items[key] = {'order': key, 'order_items': order_items, 'total_price': total_price}
            else:
                existing_order = grouped_items[key]['order']
                existing_items = grouped_items[key]['order_items']
                existing_total_price = grouped_items[key]['total_price']
                grouped_items[key] = {
                    'order': existing_order,
                    'order_items': existing_items + order_items,
                    'total_price': existing_total_price + total_price
            }
                
        return render(request,'vendor_dashboard/dashboard.html',{'list_order':list(grouped_items.values())})
    else:
        return render(request,'vendor_dashboard/redirectasV.html')

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
  
@login_required(login_url="/userP/login")  
def product_area(request) :
    products = Product.objects.filter(author=request.user)
    return render(request , 'vendor_dashboard/product_area.html',{'products' :products})

@login_required(login_url="/userP/login")
def add_product(request) :
    if request.method == 'POST' :
        form = forms.CreateProduct(request.POST , request.FILES)
        if form.is_valid() :
            instance = form.save(commit=False)
            instance.author =request.user 
            instance.save()
            return redirect('vendor_dashboard:product_area')
        else:
            return JsonResponse({'error': 'form invalid', 'errors': form.errors})    
    else :
        form = forms.CreateProduct()
    return render(request , 'vendor_dashboard/add_product.html' , {'form':form })





@login_required(login_url="/userP/login")
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = UpdateProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product=form.save()
            print(product.type_p)
            return redirect('vendor_dashboard:product_area')
        else:
            return JsonResponse({'error': 'form invalid', 'errors': form.errors})  
            
    else:
        form = UpdateProduct(instance=product)

    return render(request, 'vendor_dashboard/update_product.html', {'form': form, 'product': product})


@login_required(login_url="/userP/login")
def delete_product(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids[]')
        product_ids = [product.id for product in Product.objects.all()]
        selected_ids = [int(id) for id in selected_ids]
        products_to_delete = Product.objects.filter(id__in=selected_ids)
        products_to_delete.delete()
        return redirect('vendor_dashboard:product_area')
    else:
        return HttpResponse("<h1>Invalid method</h1>")
    

@login_required(login_url="/userP/login")
def search_product(request) :
    if request.method =='POST':
       searched = request.POST['search']
       product_search = Product.objects.filter(
        Q(type_p__icontains=searched) | Q(name__icontains=searched) | Q(color__icontains=searched) ,
        author=request.user
       )
       return render(request , 'vendor_dashboard/search_product.html',{'product_search' :product_search})
    else :
     products = Product.objects.filter(author=request.user)
    return   render(request , 'vendor_dashboard/search_product.html' , {'products':products} )


def annuler_commande (request) :
    quantities = request.GET.getlist('quantity')
    product_ids = request.GET.getlist('product_id')
    order_id = int(request.GET.get('order_id'))

    for i in range(len(product_ids)):
        product_id = int (product_ids[i])
        quantity = int(quantities[i])
        product = Product.objects.get(id=product_id)
        product.quantity += quantity
        product.save()
        if product.quantity > 0 :
                product.status = "Available" 
                product.save() 
    
    OrderItem.objects.filter(order_id=order_id, product__author=request.user).delete()

    if not OrderItem.objects.filter(order_id=order_id).exists():
        Order.objects.get(id=order_id).delete()
    return redirect('vendor_dashboard:dashboard')

def approve_command(request):
    
    order_id = int(request.GET.get('order_id'))
    OrderItem.objects.filter(order_id=order_id, product__author=request.user).delete()

    if not OrderItem.objects.filter(order_id=order_id).exists():
        Order.objects.get(id=order_id).delete()
    return redirect('vendor_dashboard:dashboard')

    
