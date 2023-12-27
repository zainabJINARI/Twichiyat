from .models import Profile

def profiles(request):
    return {'profiles':Profile.objects.all()}