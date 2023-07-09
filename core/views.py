from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def generic(request):
    return render(request, 'generic.html')