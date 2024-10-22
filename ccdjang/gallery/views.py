
# Create your views here.
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
import os

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect to your gallery view
    else:
        form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})
