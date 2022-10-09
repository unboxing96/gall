from django import forms
from .models import Gall


class GallForm(forms.ModelForm):
    class Meta:
        model = Gall
        fields = "__all__"
