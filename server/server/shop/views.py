from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def detail(request):
    return render(request, 'detail.html', {})

def order(request):
    return render(request, 'order.html', {})

def register(request):
    return render(request, 'register.html', {})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create(username=username, email=email, password=password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'success': 'Account created successfully'})
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request ,email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def email_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user.exists():
            return render(request, 'email.html', {'success': 'An email has not been sent to th address'})
        else:
            return render(request, 'email.html', {'error': 'Email does not exist in our system'})