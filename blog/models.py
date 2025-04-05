from django.db import models  # type: ignore
import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blog/images')
    # si no le paso una feha, coloca la fecha actual
    date = models.DateField(datetime.date.today)

    def __str__(self):  # metodo __str__ para retornar el los atributos del objecto
        return self.title  # retorna el nombre
