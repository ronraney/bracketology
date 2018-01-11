from django.shortcuts import render
from django.urls import path
from django.contrib.auth.decorators import login_required

# Old school index
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'blog/index.html')