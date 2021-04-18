from django import forms

class CommentForm(forms.Form):
    post = forms.CharField(
        max_length=280,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Add a comment...'}))