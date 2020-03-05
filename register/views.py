from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(req):
  if req.method == "POST":
    email = req.POST["email"]
    user = req.POST["user"]
    if User.objects.filter(email = email):
      messages.info(req,"Email Exits")
      return render(req,"signup.html")
    elif User.objects.filter(username = user):
      messages.info(req,"User name exits")
      return render(req,"signup.html")
    else:
      fname = req.POST["fname"]
      lname = req.POST["lname"]
      pass1 = req.POST["pass"]
      user = User.objects.create_user(first_name = fname,last_name = lname, username = user,email = email , password = pass1)
      user.save()
      return redirect("/login")
  else:
    if req.GET["know"] == "Know":
      messages.info(req,"You first need to signup")
      return render(req,"signup.html")
    
    else:
      return render(req,"signup.html")

  
