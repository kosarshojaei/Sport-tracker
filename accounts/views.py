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
