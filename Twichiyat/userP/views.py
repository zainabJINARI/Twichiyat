from django.shortcuts import render,redirect
from .forms import CreateUser,UserCreationForm
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if 'next' in request.POST:
                user.is_vendor=True
                return redirect('home')
    else:
        form = CreateUser()
    return render(request,'userP/signup.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        return redirect('home')
    else:
        return render(request,'userP/login.html')
        
