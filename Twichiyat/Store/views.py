from django.shortcuts import render,redirect
from .models import Collection
from vendor_dashboard.models import Product
from Store.models import Collection
from django.shortcuts import get_object_or_404
from . import forms
from django.http import HttpResponse, JsonResponse
from .models import Order,OrderItem

# Create your views here.

def shop_now(request):
    products = Product.objects.all().order_by('date')
    latest_products=[]
    if len(products)>=5:
        for i in range(len(products)-1,0,-1):
            if len(latest_products)<4:
                latest_products.append(products[i])
            else:
                break

    collections = Collection.objects.all()
    
    return render(request,'Store/home.html',{'collections':collections,'products':latest_products})

def carte(request):
    return render(request,'Store/Cartepage.html')


def file_product(request):
    return render(request,'Store/fileproduct.html')

def productlist(request):
    return render(request,'Store/product_list.html')

def product_category(request, category_id):
    category = get_object_or_404(Collection, id=category_id)
    print(category)
    products = Product.objects.filter(type_p=category)
    print(products)
    return render(request, 'Store/productByCategory.html', {'products': products, 'category': category})

def product_details(request,product_id):
    product_item = get_object_or_404(Product, id=product_id)
    return render(request,'Store/productDetail.html',{'product':product_item})

def order_product (request) :
    if request.method =='POST':
        form =forms.CreateOrder()
        note = request.POST.get('note')
        product_ids = request.POST.getlist('product_id[]')
        prodct_ids_str = ','.join(product_ids)
        product_quantities = request.POST.getlist('product_q[]')
        product_quantities_str = ','.join(product_quantities)
        return  render(request, 'Store/order.html' , {'form':form ,'note':note,'ids':prodct_ids_str,'quantities':product_quantities_str} )
    else:
        return render(request, 'Store/order.html')
    
def add_order(request):
    if request.method=='POST':
        print(request.POST)
        # name = 
       
        ids = request.POST.get('ids')
        quantities = request.POST.get('quantities')
        idslist=ids.split(',')
        proQu=quantities.split(',')
        new_order = Order.objects.create(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            phone_nbr=request.POST.get('phone_nbr'),
            postal_code=request.POST.get('postal_code'),
            note=request.POST.get('note')
        )
        # listProductFull =[]
        for i in range(len(idslist)):   
            product = get_object_or_404(Product, id=int(idslist[i]))
            product.quantity=product.quantity-int(proQu[i])
            product.save()  
            new_order_item=OrderItem.objects.create(
                order=new_order,
                product=product,
                quantity=int(proQu[i])
            )
        print(new_order)
        print(idslist)
        print(proQu)
        return redirect('Store:shopnow')
        
    else:
        return redirect('Store:order')