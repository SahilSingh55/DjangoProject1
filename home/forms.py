from django import forms
from .models import Contact

class ImageForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'image']