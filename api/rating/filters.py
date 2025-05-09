import django_filters 
from service.models import Rating

class RatingFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr='lte')

    class Meta:
        model = Rating
        fields = ['min_rating', 'max_rating']
