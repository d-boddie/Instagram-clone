from message.models import Message
from photo.models import Photo
from comment.models import Comment

def notification_processor(request):
    if request.user.is_authenticated:
        messages = Message.objects.filter(to=request.user)
        photos = Photo.objects.filter(poster=request.user).all()
        no_msgs = len(messages.filter(read=False)) 
        total = 0
        for p in photos:
            for i in p.photo.all():
                if not i.viewed:
                    total += 1
        total = total + no_msgs
    else: 
        total = 0

        
    return {
        'messages' : total
    }