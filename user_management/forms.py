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
        "placeholder": "Nama",
    }))
    referal_code = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "input100",
        "placeholder": "Referal code",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "input100",
        "placeholder": "Username",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type": "email",
        "class": "input100",
        "placeholder": "Email",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input100",
        "placeholder": "Password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input100",
        "placeholder": "Ulangi Password",
    }))

    def clean_username(self):
        obj = self.cleaned_data['username']
        if User.objects.filter(username__iexact=obj).exists():
            raise forms.ValidationError("Username sudah digunakan")

        if len(obj) <= 5:
            raise forms.ValidationError("Username harus lebih dari 5 karakter")

        return obj

    def clean_email(self):
        obj = self.cleaned_data['email']
        if Data_User.objects.filter(email__iexact=obj).exists():
            raise forms.ValidationError("Email sudah digunakan")

        return obj

    def clean_referal_code(self):
        obj = self.cleaned_data['referal_code']
        if Data_User.objects.filter(referal_code=obj).exists() == False:
            raise forms.ValidationError("Kode referal tidak ditemukan")
        return obj

    def clean_password1(self):
        obj = self.cleaned_data['password1']
        if re.search('[A-Z]', obj) == None \
                or re.search('[0-9]', obj) == None \
                or re.search('[^A-Za-z0-9]', obj) == None or len(obj) < 8:
            raise forms.ValidationError(
                "Password Harus mengandung 1 Huruf Besar, 1 Angka, dan 1 Symbol. Minimal 8 Karakter")
        return obj

    def clean_password2(self):
        obj = self.cleaned_data['password2']
        if re.search('[A-Z]', obj) == None \
                or re.search('[0-9]', obj) == None \
                or re.search('[^A-Za-z0-9]', obj) == None or len(obj) < 8:
            raise forms.ValidationError(
                "Password Harus mengandung 1 Huruf Besar, 1 Angka, dan 1 Symbol. Minimal 8 Karakter")
        return obj

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Password tidak sesuai")
