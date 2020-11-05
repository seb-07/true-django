
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect
from .forms import RegisterForm,loginform
def register(request):
    form =RegisterForm(request.POST or None)
    
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newuser=User(username=username)
        newuser.set_password(password)
        newuser.save()
        login(request,newuser)
        messages.success(request,"Başarıyla kayıt yaptınız..")
        return redirect("index")
    context ={
        "form":form
        }
    return render(request,"register.html",context)

    

def loginuser(request):
    form=loginform(request.POST or None)
    context ={
        "form":form
        }
    
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user= authenticate(username=username,password=password)
        if user is None:
            messages.warning(request,"Kullanıcı adı veya parola yanlış..")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız.")    
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)
def logoutuser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")

    return redirect("index")