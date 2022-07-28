from .models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'avatar', 'email', 'bio', 'section']


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'bio', 'section']
