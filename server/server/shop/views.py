from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def detail(request):
    return render(request, 'detail.html', {})