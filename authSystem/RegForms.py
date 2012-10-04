from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from authSystem.models import UserAccount

class RegistrationForm(ModelForm):
    username        = forms.CharField(label=(u'User Name'))
    email           = forms.EmailField(label=(u'Email Address'))
    password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = UserAccount
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("This username is already taken, please select another")

    def clean(self):
        password = self.cleaned_data.get('password', None)
        password1 = self.cleaned_data.get('password1', None)
        if password and password1 and password != password1:
            raise forms.ValidationError("Your passwords did not match, please try again")
        return self.cleaned_data

class LoginForm(forms.Form):
    username    = forms.CharField(label=(u'User Name'))
    password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))