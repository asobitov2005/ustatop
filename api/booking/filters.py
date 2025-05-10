from django_filters import rest_framework as filters
from service.models import Booking

class BookingFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='exact')  # Точный фильтр по статусу
    client = filters.NumberFilter(field_name='client', lookup_expr='exact')  # Фильтр по ID клиента
    service = filters.NumberFilter(field_name='service', lookup_expr='exact')  # Фильтр по ID услуги

    class Meta:
        model = Booking
        fields = ['status', 'client', 'service',]