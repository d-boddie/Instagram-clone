"""instagramclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/<int:user_id>', views.user_detail, name='detail'),
    path('editprofile/<int:user_id>', views.edit_profile, name='edit profile'),
    path('editaccount/<int:user_id>', views.edit_account, name='edit account'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
