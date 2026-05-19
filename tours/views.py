from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

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