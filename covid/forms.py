from django import forms

class CovidForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs=({
        'placeholder': 'Enter A State'
    })), max_length=50, required=True)