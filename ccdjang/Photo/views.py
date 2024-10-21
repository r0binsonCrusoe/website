from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Photo

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})
