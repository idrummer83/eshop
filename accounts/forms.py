from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label='login', max_length=20)
    passwd = forms.CharField(label='password', max_length=20, widget=forms.PasswordInput())
