from django.db import models
from user.models import User


class Service(models.Model):
    type = models.CharField(max_length=255, null=False, blank=False)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='provided_services')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.type


class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='bookings_as_client')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, related_name='bookings')
    scheduled_date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Booking {self.id} for {self.service}"


class Rating(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='ratings')
    rating = models.IntegerField(null=False, blank=False)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f"Rating {self.rating} by {self.user}"
