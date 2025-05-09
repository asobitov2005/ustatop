from django.db import models
from user.models import CustomUser


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Address(models.Model):
    street_name = models.CharField(max_length=100)
    booking_address = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

