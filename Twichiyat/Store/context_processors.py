from .models import Collection

def collectionslist(request):
    return {'collectionslist':Collection.objects.filter()}