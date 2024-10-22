from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')  # Files will be saved in media/photos/
    uploaded_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField() # Use a PointField for coordinates
    

    def __str__(self):
        return self.title