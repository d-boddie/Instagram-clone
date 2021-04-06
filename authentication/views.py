from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignupForm
from .models import InstagramUser

# Create your views here.

def sign_up_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = InstagramUser.objects.create_user(
                username=data['username'], 
                password=data['password'], 
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            return HttpResponseRedirect(reverse("login"))

    form = SignupForm()
    return render(request, "sign_up.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def index(request):
    post = InstagramUser.objects.all()
    return render(request, "index.html", {
        'heading': 'Profile Page', 'post': post})