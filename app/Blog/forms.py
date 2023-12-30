from django import forms
from Blog.models import Posts,User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput, label="Password"
    )


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "profile"]


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "profile"]


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["description", "image"]
