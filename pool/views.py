from django.shortcuts import render
from django.urls import path
from django.contrib.auth.decorators import login_required

# Old school index
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'blog/index.html')
	
# User list view with point totals - links to detail view of selections
# User detail view(s) with selections (available only after start date)
# Selection form view(s) - 4x4 view and Final Four
