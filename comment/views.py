from django.shortcuts import render, redirect, reverse
from .forms import CommentForm
from .models import Comment

# Create your views here.


def comment(request):
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                post=data['post']
            )
        return redirect(reverse('homepage'))

    form = CommentForm()
    return render(request, 'comments.html', {
        "form": form,
        'comments': comments})


def delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect(reverse('comments'))


def edit_view(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment.post = data['post']
            comment.save()
            return redirect(reverse('homepage'))
    form = CommentForm(initial={
            'post': comment.post,
            'likes': comment.likes
    })
    return render(request, 'edit_comments.html', {'form': form})


def likes(request, id):
    comment = Comment.objects.get(id=id)
    comment.likes += 1
    comment.save()
    return redirect(reverse('comments'))
