from django_filters import rest_framework as filters
from service.models import Rating

class RatingFilter(filters.FilterSet):
    rating = filters.NumberFilter(field_name='rating', lookup_expr='exact')  # Точный фильтр по rating
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')  # Rating >= X
    rating__lte = filters.NumberFilter(field_name='rating', lookup_expr='lte')  # Rating <= X
    # booking = filters.NumberFilter(field_name='booking', lookup_expr='exact')  # Фильтр по booking
    # created_at__gte = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')  # Created_at >= дата
    # created_at__lte = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')  # Created_at <= дата
    # comment = filters.CharFilter(field_name='comment', lookup_expr='icontains')  # Поиск по comment

    class Meta:
        model = Rating
        fields = ['rating', 'rating__gte', 'rating__lte']

# 'booking', 'created_at__gte', 'created_at__lte', 'comment'
