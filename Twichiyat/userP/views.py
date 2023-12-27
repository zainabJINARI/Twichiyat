from django.shortcuts import render,redirect
from .forms import CreateUser,UserCreationForm , AuthenticationForm
from django.contrib.auth import login


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if 'next' in request.POST:
                
                print(request.POST.get('next'))
                if request.POST.get('next') =='/dashboard/':
                    user.is_vendor=True
                    user.save()
                    login(request,user)
                    return redirect('vendor_dashboard:dashboard')
                else:
                    user.save()
                    login(request,user)
                    return redirect('home')
                
    else:
        form = CreateUser()
    return render(request,'userP/signup.html',{'form':form})


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(date=request.POST)
        if form.is_valid() :
            user=form.get_user()
            login(request , user)
            if user.is_vendor == True :
                return redirect('vendor_dashboard:dashboard')
            else :
                if 'next' in request.POST :
                    return  redirect(request.POST.get('next'))
                else :
                    pass
                    #redirect shop
                    # return redirect('')
       
    else:
        form =AuthenticationForm()
        return render(request,'userP/login.html' , { 'form':form })
        
