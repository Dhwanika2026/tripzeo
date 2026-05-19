from django.db import models

# Create your models here.
from django.db import models

class Package(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='packages/')
    offer = models.CharField(max_length=200)

    def __str__(self):
        return self.title