from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required( login_url="/userP/login")
def dashboard_home(request):
    return render(request,'vendor_dashboard/dashboard.html')
