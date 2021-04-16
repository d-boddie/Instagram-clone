from django.shortcuts import render, redirect
from authentication.models import InstagramUser
from photo.models import Photo

# Create your views here.


def avatar(request, id):
    user = InstagramUser.objects.get(username=request.user)
    photo = Photo.objects.get(id=id)
    user.avatar = photo
    user.save()
    return render(request, 'index.html')

