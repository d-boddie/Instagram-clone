from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .forms import LoginForm, SignupForm, EditProfileForm, EditAccountForm
from .models import InstagramUser
from photo.models import Photo
from comment.forms import CommentForm
from comment.models import Comment

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

@login_required
def edit_profile(request, user_id):
    context = {}
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
    edit_profile = InstagramUser.objects.get(id=current_user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit_profile.bio = data['bio']
            edit_profile.website = data['website']
            edit_profile.first_name = data['first_name']
            edit_profile.last_name = data['last_name']
            edit_profile.save()
            return redirect(reverse('homepage'))
        return render(request, 'edit.html', {"form": form})
    form = EditProfileForm(initial=initial_data)
    context.update({'form': form})
    return render(request, 'edit.html', {"header": "Edit Profile settings", 'form': form})

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

        return redirect(request.GET.get('next', 'sign_up'))        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def index(request):
    print(request.user.avatar)
    posts = InstagramUser.objects.all()
    photos = Photo.objects.all()
    photo = Photo.objects.all().first()
    comments = Comment.objects.all()
    form = CommentForm()
    data = {
        'users': posts,
        'photos': photos,
        'comments': comments,
        'form': form
    }
    return render(request, "index.html", data)


@login_required
def user_detail(request, user_id):
    posts = InstagramUser.objects.all().filter(id=user_id)
    photo = Photo.objects.all().filter(poster_id=user_id)
    # followers = 
    return render(request, "user_detail.html", {
        'heading': 'Profile Page', 
        'photo':photo, 
        'posts': posts, 
        'user_id': user_id,
         })


@login_required
def follow(request, user_id):
    current_user = InstagramUser.objects.get(username=request.user)
    following = InstagramUser.objects.get(id=user_id)
    is_following = True
    current_user.friend.add(following)
    # current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow(request, user_id):
    current_user = InstagramUser.objects.get(username=request.user)
    following = InstagramUser.objects.get(id=user_id)
    is_following = False
    current_user.friend.remove(following)
    # current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))