from django.forms import ModelForm
from app.models import TODO
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TODOForm(ModelForm):
    class Meta:
        model=TODO
        fields=['title','status','priority']


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
         model = User
         fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
