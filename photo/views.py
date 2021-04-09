from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from photo.models import Photo
from photo.forms import PhotoForm

# Create your views here.
def photo_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = PhotoForm()
        photo = Photo.objects.all()
    return render(request, 'photo.html', {'form': form, 'photo':photo})        

def photo_detail(request, photo_id):
    current_user = request.user
    photo = Photo.objects.get(id=photo_id)
    return render(request, "photo_detail.html", {'photo': photo })


def photo_delete(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect(reverse('photos'))
    
