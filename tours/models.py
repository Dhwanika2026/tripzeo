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

