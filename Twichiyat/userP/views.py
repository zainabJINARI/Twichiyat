from django.shortcuts import render,redirect
from .forms import CreateUser,UserCreationForm , AuthenticationForm
from django.contrib.auth import login 
from django.http import HttpResponse


from django.shortcuts import render,redirect
from .forms import CreateUser,UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
from .models import Profile
from . import forms



# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Créez une instance de Profile et liez-la à l'utilisateur
            profile = Profile(user=user)
            profile.is_vendor = True if request.POST.get('next') == '/dashboard/' else False
            profile.address = form.cleaned_data['address']
            profile.phone_nbr = form.cleaned_data['phone_nbr']
            profile.gender = form.cleaned_data['gender']
            profile.slugU = form.cleaned_data['slugU']
            profile.save()

            # Connectez l'utilisateur
            login(request, user)

            # Redirigez en conséquence
            if profile.is_vendor:
                return redirect('vendor_dashboard:dashboard')
            else:
                return redirect('home')

    else:
        form = CreateUser()

    return render(request, 'userP/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid() :
            user=form.get_user()
            login(request , user)
            profiles = Profile.objects.all()
            for p in profiles :
                if p.is_vendor == True :
                    return redirect('vendor_dashboard:dashboard')

            if user.is_vendor == True :
                return redirect('vendor_dashboard:dashboard')
            else :
                if 'next' in request.POST :
                    # return  redirect(request.POST.get('next'))
                    return HttpResponse("Hi")

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
 
    
    
def logout_view(request):
    logout(request)
    return redirect('home')       

        
def logout_view(request):
    logout(request)
    return redirect('home')

