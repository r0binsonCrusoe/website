
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
        form = PhotoForm(request.POST, request.FILES)  # Handle form submission
        
        if form.is_valid():
            location = request.POST.get('location')  # Get location from form data
            
            if location:  # Check if location is provided
                try:
                    # Extract longitude and latitude
                    lon, lat = map(float, location.split(','))
                    
                    # Create a Point object with EPSG:4326
                    point = Point(lon, lat, srid=4326)
                    
                    # Save the photo instance with the location
                    photo_instance = form.save(commit=False)  # Don't save to the database yet
                    photo_instance.location = point  # Assign the Point to the location field
                    photo_instance.save()  # Save it to the database
                    
                    return redirect('gallery')  # Redirect to the gallery view
                
                except ValueError as e:
                    form.add_error('location', 'Invalid coordinate format.')
                    return render(request, 'gallery/upload.html', {'form': form})
            else:
                form.add_error('location', 'Location is required.')
                return render(request, 'gallery/upload.html', {'form': form})

        else:
            print("Form is invalid:", form.errors)  # Debugging output
            return render(request, 'gallery/upload.html', {'form': form})

    else:
        form = PhotoForm()  # Create a new form instance for GET request
    
    return render(request, 'gallery/upload.html', {'form': form})


