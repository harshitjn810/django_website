from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import travelo
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1 == password2:
        
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Emailid Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
        else:
            messages.info(request,"Password didn't match. Please try again")
            return redirect('register')

       
        print('user created')
        return redirect('/')

    else:    
        print(request.session)
        print(request.session.set_expiry(300))
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        usrnm= request.POST['username']
        pd = request.POST['password']
        user = auth.authenticate(username = usrnm, password = pd)
        
        if user is not None:
            auth.login(request,user)
            print(request.session.session_key)
            return redirect('/')
        else:
            messages.info(request,'Invalide Credentials')    
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')