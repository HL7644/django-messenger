from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html', context={})

def about_view(request):
    return render(request, 'about.html', context={})

