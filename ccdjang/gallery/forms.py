from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'description','location']

def clean_location(self):
        location = self.cleaned_data.get('location')
        if location:
            try:
                lon, lat = map(float, location.split(','))
                # Optionally, you can add more validation on longitude and latitude ranges
                if not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
                    raise forms.ValidationError("Coordinates are out of range.")
            except ValueError:
                raise forms.ValidationError("Invalid coordinate format. Use 'longitude, latitude'.")

        return location