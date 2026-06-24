from django.db import models


# =========================
# DESTINATION MODEL
# =========================

class Destination(models.Model):

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to='destinations/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# =========================
# PACKAGE MODEL
# =========================


class Package(models.Model):

    PACKAGE_TYPES = (
        ('best', 'Best Seller'),
        ('custom', 'Customized'),
        ('group', 'Group Tour'),
        ('bike', 'Bike Tour'),
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE
    )

    package_type = models.CharField(
        max_length=20,
        choices=PACKAGE_TYPES
    )

    image = models.ImageField(upload_to='packages/')

    pdf = models.FileField(upload_to='package_pdfs/')

    price = models.IntegerField()

    old_price = models.IntegerField(
        blank=True,
        null=True
    )

    duration = models.CharField(max_length=50)

    rating = models.FloatField(default=4.5)

    total_reviews = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    offer = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    short_description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    description = models.TextField()

    month = models.CharField(max_length=100)

    def __str__(self):
        return self.title



# =========================
# DEPARTURE DATES
# =========================

class Departure(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='departures'
    )

    date = models.DateField()

    price = models.IntegerField()

    seats_available = models.IntegerField()

    def __str__(self):
        return f"{self.package.title} - {self.date}"


# =========================
# ITINERARY
# =========================

class Itinerary(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='itinerary'
    )

    day_number = models.IntegerField()

    title = models.CharField(max_length=200)

    description = models.TextField()

    def __str__(self):
        return f"Day {self.day_number} - {self.package.title}"


# =========================
# INCLUSIONS
# =========================

class Inclusion(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='inclusions'
    )

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


# =========================
# EXCLUSIONS
# =========================

class Exclusion(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='exclusions'
    )

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


# =========================
# HOTELS
# =========================

class Hotel(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='hotels'
    )

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    rating = models.FloatField()

    def __str__(self):
        return self.name


# =========================
# PACKAGE GALLERY IMAGES
# =========================

class PackageImage(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='package_gallery/'
    )

    def __str__(self):
        return f"Image for {self.package.title}"
    





class TourDestination(models.Model):


 name = models.CharField(max_length=200)

 slug = models.SlugField(
 unique=True,
 blank=True,
 null=True
 )

 image = models.ImageField(
    upload_to='tour-destinations/',
    blank=True,
    null=True
 )

 price = models.IntegerField(
    blank=True,
    null=True
 )

 duration = models.CharField(
    max_length=100,
    blank=True,
    null=True
 )

 location = models.CharField(
    max_length=200,
    blank=True,
    null=True
 )

 description = models.CharField(
    max_length=255,
    blank=True,
    null=True
 )

 def __str__(self):
    return self.name




class Booking(models.Model):

    package_name = models.CharField(max_length=200)

    adults = models.IntegerField(default=1)

    children = models.IntegerField(default=0)

    infants = models.IntegerField(default=0)

    travel_date = models.DateField()

    mobile = models.CharField(max_length=20)

    email = models.EmailField()

    total_price = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.package_name
    

    
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    featured_image = models.ImageField(
        upload_to='hotels/',
        blank=True,
        null=True
    )

    location = models.CharField(max_length=200)

    address = models.TextField(
        blank=True,
        null=True
    )

    short_description = models.TextField(
        blank=True,
        null=True
    )

    about_hotel = models.TextField(
        blank=True,
        null=True
    )

    map_link = models.URLField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    check_in = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    check_out = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class HotelAmenity(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='amenities'
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HotelRoom(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='rooms'
    )

    room_name = models.CharField(max_length=200)

    room_image = models.ImageField(
        upload_to='rooms/',
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    price = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )        

class Cruise(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to='cruises/'
    )

    departure_date = models.DateField()

    nights = models.IntegerField()

    origin = models.CharField(
        max_length=100
    )

    destination = models.CharField(
        max_length=100
    )

    # itinerary = models.TextField(
    #     help_text="Mumbai > Goa > Lakshadweep > Mumbai"
    # )

    ship_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    short_description = models.TextField(
        blank=True,
        null=True
    )

    featured = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

class CruiseGallery(models.Model):
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.CASCADE,
        related_name='gallery'
    )

    image = models.ImageField(
        upload_to='cruise_gallery/'
    )

class CruiseInclusion(models.Model):

    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.CASCADE,
        related_name='inclusions'
    )

    title = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.title
    
class CruiseItinerary(models.Model):
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.CASCADE,
        related_name='itineraries'
    )

    day = models.PositiveIntegerField()

    title = models.CharField(max_length=200)

    short_description = models.TextField()

    image = models.ImageField(
        upload_to='cruise_itinerary/'
    )

    def __str__(self):
        return f"Day {self.day} - {self.title}"    

