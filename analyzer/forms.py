from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ResumeAnalyzeForm(forms.Form):
    resume_file = forms.FileField()
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 8,
            'class': 'form-control',
            'placeholder': 'Paste job description here'
        })
    )

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")