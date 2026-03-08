from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import UserCreationFrom
from .models import Project, Profile, ContactMessage

class RegisterFrom(UserCreationFrom):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = [ 'username', 'email', 'password']

class ProjectForm(forms. ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class ContactMessageForm(forms.ModelForm):
    class Meta:
        models = ContactMessage
        fields = '__all__'

class profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'