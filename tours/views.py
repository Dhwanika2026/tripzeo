from django.shortcuts import render
from django.http import HttpResponse

from .models import Package

def home(request):
    packages = Package.objects.all()
    return render(request, 'index.html', {'packages': packages})

def holiday(request):
    return render(request, "holiday.html")

def flight(request):
    return render(request, "flight.html")

def cruise(request):
    return render(request, "cruise.html")

def hotel(request):
    return render(request, "hotel.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")