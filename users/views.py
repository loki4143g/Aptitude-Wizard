from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.files.storage import default_storage
import cloudinary.uploader

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already taken")
            return redirect('users:register')
        
        user = User.objects.create(
            username = username,
            first_name = firstname,
            last_name = lastname,
            email = email
        )
        user.set_password(password)
        user.save()
        messages.success(request,f"Welcome {firstname}, Your learning journey starts now! Log in to access your practice questions and quizzes")
        return redirect('users:login')
    return render(request, 'users/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username Doesn't Exists! (or) Enter Correct Username")
            return redirect('users:login')
        user = authenticate(request,username=username,password=password)
        if user is None :
            messages.error(request, "Invalid Password")
            return redirect('users:login')
        else:
            login(request,user)
            return redirect('main:home')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return render(request,'users/logout.html')

def profile(request):
    return render(request, 'users/profile.html')

def editprofile(request):
    if request.method == "POST":
        user = request.user

        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')

        
        
        if 'profile_image' in request.FILES:
            image = request.FILES.get('profile_image')
            response = cloudinary.uploader.upload(image, folder="profilepictures")
            user.profile.image = response["secure_url"]

        
        
        user.save()
        user.profile.save()

        messages.success(request, "Changes Saved Sucessfully")
        return redirect('users:profile')

    return render(request, 'users/editprofile.html')