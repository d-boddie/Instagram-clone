from django.shortcuts import render
from photo.models import Photo

# Create your views here.
def photo_view(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos
    }
    return render(request, 'photo.html', context)