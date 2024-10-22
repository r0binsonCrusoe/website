
# Create your views here.
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib.gis.geos import Point
from django.contrib import messages  # To show user-friendly error messages
import os

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            location_data = request.POST.get('location')    
            if location_data:
                # Split the coordinates and create a Point
                longitude, latitude = map(float, location_data.split(','))
                point = Point(longitude, latitude)  # Create a Point object
            
                # Save the photo with the point location
                photo = form.save(commit=False)
                photo.location = point  # Assign the Point to the location field
                photo.save()
                messages.success(request, 'Photo uploaded successfully!')
        else:
            # If the form is not valid, return the same template with errors
            return render(request, 'gallery/upload.html', {'form': form})

    else:
        form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})

