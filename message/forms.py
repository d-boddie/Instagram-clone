from django import forms

class MessageForm(forms.Form):

    message = forms.CharField(
        max_length=280,
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Add a Message...'}))
