from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import TourDestination

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

def terms_conditions(request):
    return render(request, 't&c.html')

def policy(request):
    return render(request, "policy.html")



from django.shortcuts import render
from .models import Package


def destination_packages(request, location):

    packages = Package.objects.filter(
        destination__name__iexact=location
    )

    duration = request.GET.get('duration')
    month = request.GET.get('month')
    sort = request.GET.get('sort')

    if duration:
        packages = packages.filter(duration=duration)

    if month:
        packages = packages.filter(month=month)

    if sort == 'low':
        packages = packages.order_by('price')

    elif sort == 'high':
        packages = packages.order_by('-price')

    elif sort == 'rating':
        packages = packages.order_by('-rating')

    best_packages = packages.filter(package_type='best')

    custom_packages = packages.filter(package_type='custom')

    group_packages = packages.filter(package_type='group')

    bike_packages = packages.filter(package_type='bike')

    context = {
        'location': location,
        'best_packages': best_packages,
        'custom_packages': custom_packages,
        'group_packages': group_packages,
        'bike_packages': bike_packages,
    }

    return render(
        request,
        'destination_packages.html',
        context
    )
def package_detail(request, slug):

    package = get_object_or_404(
        Package,
        slug=slug
    )

    return render(
        request,
        'package.html',
        {
            'package': package
        }
    )

def search_destination(request):

    destination = request.GET.get('destination')

    if destination:

        packages = Package.objects.filter(
            destination__name__iexact=destination
        )

        # IF PACKAGE EXISTS
        if packages.exists():

            return redirect(
                'destination_packages',
                location=destination
            )

        # IF PACKAGE NOT FOUND
        else:
         return redirect('home')
        
def home(request):

 destinations = TourDestination.objects.all()

 return render(request, 'index.html', {
    'destinations': destinations
})        