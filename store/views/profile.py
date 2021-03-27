from django.shortcuts import render
from django.views import View

def profile(request):
    return render(request,'profile.html')