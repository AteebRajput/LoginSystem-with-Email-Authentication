from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from loginSysem import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def home(request):
    
    return render(request,'home.html')

def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            # request.session['username'] = username
            username = user.get_username()
            return render(request,'home.html',{'username':username})
        else:
            messages.info(request,'username or password is incorrect')
            # return HttpResponse("Username or Password is incorrect")
    context = {}
    
    return render(request,'login.html',context)

def register(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request,'Account has been created for ' + name +'. We have sent you a email. Please confirm your account')
            
            subject = 'Welcome to My App'
            message = "Hello "+ name + "!!! This is your confirmation email \n Thank you for using our website."
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            print(email)
            send_mail(subject,message,from_email,to_list,fail_silently=True )
            
            return redirect('/login')
    
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def signout(request):
    logout(request)
    messages.success(request,'You are successfully Logged Out')
    return redirect('home')