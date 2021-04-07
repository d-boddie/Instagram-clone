from django.shortcuts import render, HttpResponseRedirect
from photo.models import Photo
from photo.forms import PhotoForm

# Create your views here.
def photo_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            photo_obj = form.instance
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = PhotoForm()
        photo = Photo.objects.all()
    return render(request, 'photo.html', {'form': form, 'photo':photo})        