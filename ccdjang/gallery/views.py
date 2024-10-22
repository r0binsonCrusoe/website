
# Create your views here.
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib.gis.geos import Point
import os

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            location = request.POST.get('location')    
            if location:
                try:
                    lon, lat = map(float, location.split(','))
                    # Create a Point object
                    point = Point(lon, lat)
                    # Save the photo with the Point
                    photo_instance = form.save(commit=False)  # Don't save to the database yet
                    photo_instance.location = point  # Assign the Point to the location field
                    photo_instance.save()  # Now save it to the database
                    return redirect('gallery')
                except ValueError:
                    form.add_error('location', 'Invalid coordinate format.')
                    return render(request, 'gallery/upload.html', {'form': form})
                    
        else:
            # If the form is not valid, return the same template with errors
            return render(request, 'gallery/upload.html', {'form': form})

    else:
        form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})

