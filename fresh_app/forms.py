from django import forms
from django.forms import ValidationError
from django.core import validators
from django.contrib.auth.models import User
from fresh_app.models import user_profileInfo


class FormName(forms.Form):
    name = forms.CharField(max_length=243)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password",)


class user_Profileform(forms.ModelForm):
    class Meta:
        model = user_profileInfo
        fields = ("profile_pic", "portfolio_url")

