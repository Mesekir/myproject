# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! I am in the home page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Hello World! I am in the about page")
    return render(request, 'about.html')