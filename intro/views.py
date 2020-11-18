from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'intro/index.html')