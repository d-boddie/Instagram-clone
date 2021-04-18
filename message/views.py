from django.shortcuts import render, HttpResponseRedirect
from .forms import MessageForm
from .models import Message
from authentication.models import InstagramUser
from django.views.decorators.http import require_http_methods
from comment.models import Comment
from photo.models import Photo

# Create your views here.
@require_http_methods(["POST"])
def messages(request, id):
    to = InstagramUser.objects.get(id=id)
    form = MessageForm(request.POST)
    
    if form.is_valid():
        data = form.cleaned_data
        message = Message.objects.create(
            message=data['message'],
            to=to,
            creator=request.user
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def message_view(request):
    inbox = Message.objects.all().filter(to=request.user)
    sent = Message.objects.all().filter(creator=request.user)
    form = MessageForm()
    data = {
        'inbox': inbox,
        'sent': sent,
        'form': form
    }
    return render(request, 'message.html', data)


def new_notice(request):
    messages = Message.objects.all().filter(to=request.user)
    new = messages.filter(read=False)
    photos = Photo.objects.filter(poster=request.user).all()
    comments = []
    for p in photos:
        for i in p.photo.all():
            if i.viewed == False:
                comments.append(i)
    data = {
        'new': new,
        'comments': comments
    }
    
    make_true = list(comments)

    for c in make_true:
        c.viewed = True
        c.save()

    for m in new:
        m.read = True
        m.save()
    return render(request, 'new-notices.html', data)
