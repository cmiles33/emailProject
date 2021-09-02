from django import forms
from .models import Reponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Fieldset,ButtonHolder,Submit,Field

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ('textresponse',)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
