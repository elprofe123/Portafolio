from django.db import models  # type: ignore
from cloudinary.models import CloudinaryField  # type: ignore
# Create your models here.
# clase para proyecto


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='portafolio/images')
    url = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    image = CloudinaryField('image' ,blank=True, null=True,default="https://res.cloudinary.com/tu_cloud_name/image/upload/v12345678/default_image.jpg")

    def __str__(self):
        return self.title