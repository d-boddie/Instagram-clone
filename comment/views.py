from django.shortcuts import render, redirect, reverse
from .forms import CommentForm
from .models import Comment

# Create your views here.


def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                post=data['post']
            )
        return redirect(reverse('homepage'))

    form = CommentForm()
    return render(request, 'comments.html', {"form": form})
    