from django_filters import rest_framework as filters
from service.models import Rating

class RatingFilter(filters.FilterSet):
    rating = filters.NumberFilter(field_name='rating', lookup_expr='exact')  # Точный фильтр по rating
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')  # Rating >= X
    rating__lte = filters.NumberFilter(field_name='rating', lookup_expr='lte')  # Rating <= X
    booking = filters.NumberFilter(field_name='booking', lookup_expr='exact')  # Фильтр по booking

    class Meta:
        model = Rating
        fields = ['rating', 'rating__gte', 'rating__lte', 'booking']