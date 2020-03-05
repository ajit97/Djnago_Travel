from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def signin(request):
  if request.method == "POST":
    user1 = request.POST["user"]
    pass1 = request.POST["pass"]
    value = auth.authenticate(username = user1,password = pass1)
    if value is not None:
      auth.login(request,value)
      messages.info(request,request.user.is_authenticated)
      return redirect("/")
    else:
      messages.error(request,"False cradentials")
      return render(request,"signin.html")
  else:
    return render(request,"signin.html")

def logout(request):
  auth.logout(request)
  return redirect("/")