from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import TourDestination
from .models import Hotel
from .models import Package
from .models import Cruise

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
    hotels = Hotel.objects.all()

    return render(
        request,
        'hotel.html',
        {
            'hotels': hotels
        }
    )
def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def terms_conditions(request):
    return render(request, 't&c.html')

def policy(request):
    return render(request, "policy.html")

def event(request):
    return render(request, "event.html")

def sport(request):
    return render(request, "sport.html")

def villa(request):
    return render(request, "villa.html")

def tour(request):
    return render(request, "tour.html")

def forex(request):
    return render(request, "forex.html")

def cab(request):
    return render(request, "cab.html")

def insurance(request):
    return render(request, "insurance.html")

# def holiday(request):
#     return render(request, "holiday.html")

def visa(request):
    return render(request, "visa.html")





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




def package_booking(request, pk):

    package = Package.objects.get(id=pk)

    if request.method == "POST":

        adults = int(request.POST.get('adults'))

        children = int(request.POST.get('children'))

        infants = int(request.POST.get('infants'))

        travel_date = request.POST.get('travel_date')

        mobile = request.POST.get('mobile')

        email = request.POST.get('email')

        # PRICE CALCULATION

        adult_total = adults * package.price

        child_total = children * (package.price * 0.7)

        infant_total = infants * 10000

        subtotal = adult_total + child_total + infant_total

        gst = subtotal * 0.05

        grand_total = subtotal + gst

        booking = Booking.objects.create(

            package_name=package.title,

            adults=adults,

            children=children,

            infants=infants,

            travel_date=travel_date,

            mobile=mobile,

            email=email,

            total_price=grand_total

        )

        return render(

            request,

            'booking_summary.html',

            {

                'package': package,

                'booking': booking,

                'subtotal': subtotal,

                'gst': gst,

                'grand_total': grand_total

            }

        )

    return render(

        request,

        'package_detail.html',

        {

            'package': package

        }

    )

def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)

    return render(
        request,
        'hotel_detail.html',
        {
            'hotel': hotel
        }
    )

from django.shortcuts import get_object_or_404

def cruise_detail(request, slug):
    cruise = get_object_or_404(
        Cruise,
        slug=slug
    )

    return render(
        request,
        'cruise_detail.html',
        {
            'cruise': cruise
        }
    )

def cruise(request):

    cruises = Cruise.objects.all().order_by('departure_date')

    return render(
        request,
        'cruise.html',
        {
            'cruises': cruises
        }
    )