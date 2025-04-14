# accounts/views.py

from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود به سیستم پس از ثبت‌نام
            return redirect('home')  # یا هر URL که می‌خواهید
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # یا هر URL که می‌خواهید
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})

from django.contrib.auth.forms import UserChangeForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


from django.shortcuts import render, redirect
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        password = request.POST['password']  # تو پروژه واقعی باید هش بشه

        # ذخیره در دیتابیس
        UserProfile.objects.create(
            username=username,
            email=email,
            phone=phone,
            gender=gender,
            birthdate=birthdate,
            password=password
        )
        return redirect('login')  # بعد از ثبت‌نام می‌ره به صفحه لاگین

    return render(request, 'signup.html')

