import re
from django import forms
from .models import *

class Register_Form(forms.Form):
    pos = (
        ('0','KANAN'),
        ('1','KIRI')
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "input100",
        "placeholder": "Your Name",
    }))
    referal_code = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "input100",
        "placeholder": "Referal code",
        'onKeyDown': "if(event.keyCode === 32) return false;"

    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "input100",
        "placeholder": "Username",
        'onKeyDown': "if(event.keyCode === 32) return false;"

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type": "email",
        "class": "input100",
        "placeholder": "Email",
        'onKeyDown': "if(event.keyCode === 32) return false;"

    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input100",
        "placeholder": "Password",
        'onKeyDown': "if(event.keyCode === 32) return false;"

    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input100",
        "placeholder": "Re-type Password",
        'onKeyDown': "if(event.keyCode === 32) return false;"

    }))

    def clean_username(self):
        obj = self.cleaned_data['username']
        if User.objects.filter(username__iexact=obj).exists():
            raise forms.ValidationError("Username Already Exists")

        if len(obj) <= 5:
            raise forms.ValidationError("Username must be more than 5 character")

        return obj

    def clean_email(self):
        obj = self.cleaned_data['email']
        if Data_User.objects.filter(email__iexact=obj).exists():
            raise forms.ValidationError("Email already exists")

        return obj

    def clean_referal_code(self):
        obj = self.cleaned_data['referal_code']
        if Data_User.objects.filter(referal_code=obj).exists() == False:
            raise forms.ValidationError("Invalid Referal Code")
        return obj

    def clean_password1(self):
        obj = self.cleaned_data['password1']
        if re.search('[A-Z]', obj) == None \
                or re.search('[0-9]', obj) == None \
                or re.search('[^A-Za-z0-9]', obj) == None or len(obj) < 8:
            raise forms.ValidationError(
                "Password must contain 1 Uppercase, 1 Number, and 1 Symbol. Minimum 8 Character")
        return obj

    def clean_password2(self):
        obj = self.cleaned_data['password2']
        if re.search('[A-Z]', obj) == None \
                or re.search('[0-9]', obj) == None \
                or re.search('[^A-Za-z0-9]', obj) == None or len(obj) < 8:
            raise forms.ValidationError(
                "Password must contain 1 Uppercase, 1 Number, and 1 Symbol. Minimum 8 Character")
        return obj

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Password does'nt match")
