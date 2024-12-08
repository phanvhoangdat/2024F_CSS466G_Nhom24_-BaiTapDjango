from .models import Post
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        print(f"Username: {username}")
        if user is not None:
            print(f"Username: {username} Password {password}")
            login(request=request,user=user)
            return render(request,"mgm_template/home.html")

        else:
            return render(request,"mgm_template/login.html",{'error': 'Invalid credentials.'})

        
    return render(request, "mgm_template/login.html")

def register(request):
    
    if request.method == "POST":
        username = request.POST.get("new Username")
        password = request.POST.get("new Password")
        rp_password = request.POST.get("repeat Password")
        email = request.POST.get("email")
        print(f"{username} {password} {email}")
        if password != rp_password:
            messages.error(request,"Password do not match")
            return render(request,"mgm_template/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username is already exists")
            return render(request,"mgm_template/register.html")
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return render(request,"mgm_template/login.html")    
    return render(request, "mgm_template/register.html")


def logout_page(request):
    logout(request)
    return render(request,"mgm_template/login.html")


def home(request):
    login_required()
    post = Post.objects.all()
    context = {
        'blog':post
    }
    return render(request,"mgm_template/home.html",context=context)

def dashboard(request):
    users = User.objects.all()
    return render(request,"mgm_template/dashboard.html",{"users":users})

