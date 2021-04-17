from django import forms
from .models import InstagramUser


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
        
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    
    last_name = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
   
    username = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = InstagramUser
        fields = [
            "bio",
            "email",
            "website",
            "first_name",
            "last_name",
            'avatar'
        ]


class EditAccountForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput) 
