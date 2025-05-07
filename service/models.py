from django.db import models
from user.models import CustomUser


class Service(models.Model):
    SERVICE_TYPE_CHOICES = (
        ('cleaning', 'cleaning'),
        ('plumbing', 'plumbing'),
        ('electricians', 'electricians')
    )

    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    description = models.CharField(max_length=300, null=True, blank=True)
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f'Client: {self.provider} - va u uchin service {self.service_type}'


class Booking(models.Model):
    STATUS_CHOICES = (
        ('tolanmoqda', 'tolanmoqda'),
        ('tolab bo\'ingan', 'tolab bo\'ingan'),
        ('tugatilgan', 'tugatilgan'),
        ('bekor qilingan', 'bekor qilingan'),
    )
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField()


    def __str__(self):
        return f'Booking qilingan {self.status} client {self.client} - {self.date}'


class Rating(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}'







