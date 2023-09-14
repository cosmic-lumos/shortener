from django import forms
from url.models import Url

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['link']