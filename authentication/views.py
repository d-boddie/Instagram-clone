from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .forms import LoginForm, SignupForm
from .models import InstagramUser

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


def edit_profile(request, user_id):
    context = {}
    current_user = request.user
    initial_data = {
        'username': current_user.username,
        'password': current_user.password,
        'email': current_user.email,
        'first_name': current_user.first_name,
        'last_name': current_user.last_name
        }
    edit_profile = InstagramUser.objects.get(id=current_user.id)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
<<<<<<< HEAD
            edit_profile.username = data['username']
            edit_profile.password = data['password']
=======
            edit_profile.bio = data['bio']
            edit_profile.website = data['website']
>>>>>>> 71277be1c31d53a62d98eda2fae25e38321e2402
            edit_profile.email = data['email']
            edit_profile.first_name = data['first_name']
            edit_profile.last_name = data['last_name']
            edit_profile.save()
            return redirect(reverse('homepage'))
        return render(request, 'sign_up.html', {"form": form})
    form = SignupForm(initial=initial_data)
    context.update({'form': form})
<<<<<<< HEAD
    return render(request, 'sign_up.html', {'form': form})

=======
    return render(request, 'sign_up.html', {"header": "Edit Profile settings", 'form': form})

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
        return render(request, 'sign_up.html', {"header": "Edit Account settings", "form": form})
    form = EditAccountForm(initial=initial_data)
    context.update({'form': form})
    return render(request, 'sign_up.html', {"header": "Edit Account settings", 'form': form})
>>>>>>> 71277be1c31d53a62d98eda2fae25e38321e2402

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
                return redirect(request.GET.get('next', '/'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def index(request):
    posts = InstagramUser.objects.all()
    return render(request, "index.html", {
        'heading': "Here's who you could be following:", 'posts': posts })

def user_detail(request, user_id):
    current_user = request.user
    posts = InstagramUser.objects.filter(id=user_id)
    return render(request, "user_detail.html", {
        'heading': 'Profile', 'posts': posts })


def follow(request, user_id):
    current_user = request.user
    following = InstagramUser.objects.get(id=user_id)
    current_user.follow.add(following)
    is_following = True
    return HttpResponseRedirect(reverse('homepage'))

def unfollow(request, user_id):
    current_user = request.user
    following = InstagramUser.objects.get(id=user_id)
    current_user.follow.remove(following)
    is_following = False
    return HttpResponseRedirect(reverse('homepage'))