from django.shortcuts import render
from .models import Collection
from vendor_dashboard.models import Product
from Store.models import Collection
from django.shortcuts import get_object_or_404
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