from django.shortcuts import render

# Create your views here.

def shop_now(request):
    return render(request,'Store/home.html')