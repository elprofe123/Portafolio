import os
from django.shortcuts import render #type: ignore
from .models import Project

from django.contrib.auth.models import User # type: ignore
# Crear superusuario basado en variables de entorno
username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
password = os.getenv('ADMIN_PASSWORD', '123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username, email=email, password=password)
    print(f"Superusuario '{username}' creado exitosamente.")
# if not User.objects.filter(username='admin').exists():
#     User.objects.create_superuser('admin', 'admin@example.com', '123')
#     print("Superusuario creado exitosamente")

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',{'projects':projects})