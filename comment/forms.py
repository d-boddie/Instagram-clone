from django import forms

class CommentForm(forms.Form):
    post = forms.CharField(widget=forms.Textarea, max_length=280)