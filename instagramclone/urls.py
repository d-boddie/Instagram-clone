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
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authentication import views
from comment.views import comment, delete, edit_view, likes
from photo.views import photo_view, photo_detail, photo_delete, photo_like
from about.views import about
from covid.views import covid
from dogs.views import dogs
from user.views import avatar
from news.views import news
from shoes.views import shoes
from message.views import messages, message_view, new_notice, chat


urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='homepage'),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('user/<int:user_id>', views.user_detail, name='detail'),
    path('delete-user/<int:user_id>', views.delete_user, name='delete-user'),
    path('editprofile/<int:user_id>', views.EditProfileView.as_view(), name='edit profile'),
    path('editaccount/<int:user_id>', views.edit_account, name='edit account'),
    path('follow/<int:user_id>', views.follow, name="follow"),
    path('unfollow/<int:user_id>', views.unfollow, name="unfollow"),
    path('comment/<int:id>/', comment, name='comments'),
    path('delete-comment/<int:id>/', delete, name='delete'),
    path('edit-comment/<int:id>/', edit_view, name='editcomment'),
    path('likes/<int:id>/', likes, name='likes'),
    path('photo/', photo_view, name='photos'),
    path('photo/<int:photo_id>/', photo_detail, name='photo detail'),
    path('deletephoto/<int:id>/', photo_delete, name='photo delete'),
    path('photolikes/<int:id>/', photo_like, name='photo like'),
    path('about/', about, name='about'),
    path('covid/', covid, name='covid'),
    path('dogs/', dogs, name='dogs'),
    path('avatar/<int:id>/', avatar, name='avatar'),
    path('news/', news, name='news'),
    path('shoes/', shoes, name='shoes'),
    path('create-message/<int:id>/', messages, name='messages'),
    path('message/', message_view, name='messages'),
    path('new-notices/', new_notice, name='new-messages'),
    path('chat/<int:id>/', chat, name='chat'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)