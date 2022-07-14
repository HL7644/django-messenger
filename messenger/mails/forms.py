from django import forms
from .models import Mail

class Mail_Form(forms.ModelForm):
    from_user=forms.CharField(label="My Username",  widget=forms.TextInput(attrs={
        'class':'form-control my-2',
    }))
    to_user=forms.CharField(label="Send To",  widget=forms.TextInput(attrs={
        'class':'form-control my-2',
        'placeholder': 'To Username:',
    }))
    title=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control my-2',
        'placeholder': 'Title',
    }))
    body=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control my-2',
        'placeholder': 'Content',
    }))
    class Meta:
        model=Mail
        fields=[
            'from_user',
            'to_user',
            'title',
            'body',
        ]