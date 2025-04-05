from django.shortcuts import render #type: ignore
from .models import Proyect
# Create your views here.
def home(request):
    projects=Proyect.objects.all()
    return render(request,'home.html',{'projects':projects})