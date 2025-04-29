from django.db import models  # type: ignore
import datetime
from cloudinary.models import CloudinaryField  # type: ignore
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    #image = models.ImageField(upload_to='blog/images')
    image = CloudinaryField('image' ,blank=True, null=True,default="https://res.cloudinary.com/tu_cloud_name/image/upload/v12345678/default_image.jpg")

    # si no le paso una feha, coloca la fecha actual
    date = models.DateField(datetime.date.today)

    def __str__(self):  # metodo __str__ para retornar el los atributos del objecto
        return self.title  # retorna el nombre
