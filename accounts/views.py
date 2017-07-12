from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.

def profile(request):
	return render(request, 'accounts/profile.html')
