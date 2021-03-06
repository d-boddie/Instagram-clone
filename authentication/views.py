from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, SignupForm, EditProfileForm, EditAccountForm
from .models import InstagramUser
from photo.models import Photo
from comment.forms import CommentForm
from comment.models import Comment
from message.forms import MessageForm
from message.models import Message

# Create your views here.


class SignUpView(View):
    def get(self, request):
        template_name = "sign_up.html"
        form = SignupForm()
        return render(request, template_name, {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = InstagramUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email')
            )
            login(request, new_user)
            return redirect(reverse('homepage'))

# @login_required
class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        current_user = request.user

        initial_data = {
            'username': current_user.username,
            'password': current_user.password,
            'bio': current_user.bio,
            'website': current_user.website,
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name
        }    

        template_name = "edit.html"
        form = EditProfileForm(initial=initial_data)
        return render(request, template_name, 
            {"header": "Edit Profile settings", 'form': form})

    def post(self, request, user_id):
        current_user = request.user
        edit_profile = InstagramUser.objects.get(id=current_user.id)
        form = EditProfileForm(request.POST, request.FILES, instance=edit_profile)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            data = form.cleaned_data
            edit_profile.bio = data['bio']
            edit_profile.website = data['website']
            edit_profile.first_name = data['first_name']
            edit_profile.last_name = data['last_name']
            edit_profile.avatar = data['avatar']
            edit_profile.save()
            return redirect(reverse('homepage'))

        
        
@login_required
def edit_account(request, user_id):
    context = {}
    current_user = request.user
    initial_data = {
        'username': current_user.username,
        'password': current_user.password,
    }
    edit_account = InstagramUser.objects.get(id=current_user.id)
    if request.method == 'POST':
        form = EditAccountForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit_account.username = data['username']
            edit_account.password = data['password']
            edit_account.save()
            return redirect(reverse('homepage'))
        return render(request, 'edit.html', {"header": "Edit Account settings", "form": form})
    form = EditAccountForm(initial=initial_data)
    context.update({'form': form})
    return render(request, 'edit.html', {"header": "Edit Account settings", 'form': form})


class LoginView(View):
    def get(self, request):
        template_name = "login.html"
        form = LoginForm()
        return render(request, template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = authenticate(
                request, username=data.get('username'), password=data.get('password')
            )
            if new_user:
                login(request, new_user)
                return redirect(request.GET.get('next', 'homepage'))

        return redirect('login')        

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required
def index(request):
    current_user = InstagramUser.objects.get(username=request.user)
    current_user.friends.add(current_user)
    current_user.save()
    posts = InstagramUser.objects.all()
    photos = Photo.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')[0:2]
    all_comments = Comment.objects.all()
    form = CommentForm()
    data = {
        'users': posts,
        'photos': photos,
        'comments': comments,
        'form': form,
        'all_comments': all_comments
    }
    return render(request, "index.html", data)


@login_required
def user_detail(request, user_id):
    posts = InstagramUser.objects.all().filter(id=user_id)
    post = InstagramUser.objects.get(id=user_id)
    friend = InstagramUser.objects.get(id=user_id)
    photo = Photo.objects.all().filter(poster_id=user_id)
    form = MessageForm()
    follows = friend.friends.all()[1:]
    friends = friend.following.all()
    print(request.user.friends.all())
    return render(request, "user_detail.html", {
        'heading': 'Profile Page', 
        'photo':photo, 
        'posts': posts, 
        'user_id': user_id,
        'form': form,
        'following': post.friends.count() - 1,
        'number': photo.count(),
        'follows': follows,
        'friends': friends
         })


@login_required
def follow(request, user_id):
    current_user = InstagramUser.objects.get(username=request.user)
    following = InstagramUser.objects.get(id=user_id)
    is_following = True
    current_user.friends.add(following)
    following.following.add(current_user)
    following.save()
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow(request, user_id):
    current_user = InstagramUser.objects.get(username=request.user)
    following = InstagramUser.objects.get(id=user_id)
    is_following = False
    current_user.friends.remove(following)
    following.following.remove(current_user)
    following.save()
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_user(request, user_id):
    account = InstagramUser.objects.get(id=user_id)
    account.delete()
    return redirect(reverse('sign_up'))
