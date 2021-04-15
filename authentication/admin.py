from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import InstagramUser

# Register your models here.

class InstagramUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = InstagramUser
    list_display = ['username','email', 'display_name', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name')
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (['display_name', 'friends','website', 'bio', 'avatar'])
        }),
    )

    
admin.site.register(InstagramUser, InstagramUserAdmin)


