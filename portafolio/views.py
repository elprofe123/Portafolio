import os
from django.shortcuts import render #type: ignore
from .models import Project

from django.contrib.auth.models import User # type: ignore

# Cambiar la contraseña del usuario 'profe'
user = User.objects.get(username='profe')
user.set_password('rodrigo123')
user.save()

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',{'projects':projects})