from django import forms
from .models import InstagramUser


class LoginForm(forms.Form):
<<<<<<< HEAD
    username = forms.CharField(max_length=50, label='')
    password = forms.CharField(widget=forms.PasswordInput, label='')
=======
    username = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
>>>>>>> profile_page_branch
    

class SignupForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = InstagramUser
        fields = [
            "bio",
            "website",
            "first_name",
            "last_name"
        ]

class EditAccountForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)