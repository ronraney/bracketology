from django.shortcuts import render
from django.urls import path

# Old school index
def index(request):
    return render(request, 'blog/index.html')