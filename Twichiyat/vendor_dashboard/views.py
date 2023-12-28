from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from userP.models import Profile
# Create your views here.
@login_required( login_url="/userP/login")
def dashboard_home(request):
    return render(request,'vendor_dashboard/dashboard.html')


def delete_account_view(request):
    if request.method == 'POST' and request.is_ajax():
        # Effectuez la logique de suppression du compte ici
        current_profile = Profile.objects.get(user=request.user)
        current_profile.user.delete()
        
        return JsonResponse({'message': 'Account deleted successfully.'})
    return render(request, 'delete_account.html')
