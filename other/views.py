from django.shortcuts import render
from django.http import HttpResponse
from travelling.models import Locations

list = []

def article_detail(request,slug):
  object = Locations.objects.all()
  value = ""
  for obj in object:
    if obj.name.lower()==slug.lower():
      value = obj
      break
      
  return render(request,"article.html",{"obj":value})


def cart(request):
  object = Locations.objects.all()
  
  return render(request,"cart.html")