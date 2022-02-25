from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={'size': '40'}))
    password = forms.CharField(label="", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control'}))

