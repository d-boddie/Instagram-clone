from django.shortcuts import render, HttpResponseRedirect
from .forms import MessageForm
from .models import Message
from authentication.models import InstagramUser
from django.views.decorators.http import require_http_methods

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
