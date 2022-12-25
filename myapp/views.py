from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.method== "POST":
        username = request.POST.get('username')
        pass1= request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username and password incorrect!!!")
        
    return render(request,'myapp/login.html')


@login_required(login_url='login')
def homepage(request):
    return render(request, 'myapp/home.html')


def signupPage(request):
    if request.method== 'POST':
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('Your password not matched')
        else:
            my_user =User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
        
        print(uname,email, pass1, pass2)
    
    
    return render(request, 'myapp/signup.html')


def logoutPage(request):
    logout(request)
    return redirect('login')