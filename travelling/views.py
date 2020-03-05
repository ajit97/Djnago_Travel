from django.shortcuts import render
from .models import Locations

def index(request):
  obj = Locations.objects.all()
  return render(request,"index.html",{"lists": obj})
