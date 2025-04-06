import os
from django.shortcuts import render #type: ignore
from .models import Project

from django.contrib.auth.models import User # type: ignore

# Crear el usuario si no existe
if not User.objects.filter(username='profe').exists():
    User.objects.create_superuser(
        username='profe',
        email='profe@example.com',
        password='rodrigo123'
    )

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',{'projects':projects})