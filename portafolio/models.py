from django.db import models  # type: ignore

# Create your models here.
# clase para proyecto


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portafolio/images')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
