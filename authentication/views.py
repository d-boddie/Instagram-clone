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
    post = InstagramUser.objects.all()
    return render(request, "index.html", {
        'heading': 'Profile Page', 'post': post})