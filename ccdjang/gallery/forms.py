from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'description','location']

def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location:
            raise forms.ValidationError("Location is required.")
        # Additional validation can be added here
        return location