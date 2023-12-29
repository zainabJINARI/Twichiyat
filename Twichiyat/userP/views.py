from django.shortcuts import render,redirect
from .forms import CreateUser,UserCreationForm , AuthenticationForm
from django.contrib.auth import login , authenticate
from django.http import HttpResponse, JsonResponse


from django.shortcuts import render,redirect
from .forms import CreateUser , AuthenticationForm
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
                return redirect('Store:shopnow')

    else:
        form = CreateUser()
    return render(request, 'userP/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid() :
            user=form.get_user()
            current_profile = Profile.objects.get(user=user)
            login(request , user)
            if  current_profile.is_vendor == True:
                return redirect('vendor_dashboard:dashboard')
            else :
                return redirect('Store:shopnow')
        else:
            errors = {field: form.errors[field] for field in form.errors}
            error_str = str(errors)
            errors=error_str.split("'")[3]
            form =AuthenticationForm()
            if 'next' in request.POST:
                print(request.POST)
                request.GET.get('next', request.POST.get('next')) 
                return render(request, 'userP/login.html', {'form': form, 'errors': errors, 'next_param': request.POST.get('next')})
       
    else:
        form =AuthenticationForm()
        return render(request,'userP/login.html' , { 'form':form ,'errors':'' })
 
    
    
def logout_view(request):
    logout(request)
    return redirect('home')       

        


