from django import forms
from .models import Room
class addRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("name", "slug", "imgUrl")