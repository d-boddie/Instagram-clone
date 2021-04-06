from django.shortcuts import render
from photo.models import Photo
from photo.forms import PhotoForm

# Create your views here.
def photo_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
        return render(request, 'photo.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PhotoForm()
    return render(request, 'photo.html', {'form': form})        