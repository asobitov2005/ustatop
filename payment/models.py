from django.db import models
from user.models import CustomUser
from service.models import Service


class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('paid', 'paid'),
    )
    METHOD_CHOICES = (
        ('cash', 'cash'),
        ('card', 'card'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='in the process of payment')
    payment_method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()


    def __str__(self):
        return str(self.user)