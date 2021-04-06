from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.EmailField(widget=forms.EmailInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField(max_length=20)
    las_name = forms.CharField(max_length=20)