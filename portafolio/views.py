import os
from django.shortcuts import render #type: ignore
from .models import Project

from django.contrib.auth.models import User # type: ignore


# Código temporal para crear un superusuario
if not User.objects.filter(username="profe").exists():
    User.objects.create_superuser("profe","contraseña_segura")
    print("Superusuario creado: profe")

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',{'projects':projects})