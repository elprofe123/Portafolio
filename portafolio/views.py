from django.shortcuts import render #type: ignore
from .models import Project

from django.contrib.auth.models import User # type: ignore

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '123')
    print("Superusuario creado exitosamente")

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',{'projects':projects})