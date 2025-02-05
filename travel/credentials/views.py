from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        Fname= request.POST['first_name']
        Lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['conform_password']

        if password== cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('register')
            user=User.objects.create_user(username=username,first_name=Fname,last_name=Lname,email=email,password=password)
            user.save();
            return redirect('login')
            print('user created')
        else:
            messages.info(request,"passwoard not match")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid password")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
