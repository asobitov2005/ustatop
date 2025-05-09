from django.contrib import admin
from .models import Booking, Rating, Service



class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'provider', 'price', 'description')
    list_filter = ('service_type', 'provider', 'price')
    search_fields = ('service_type', 'provider__username', 'description')
    def filteration(self, request, queryset):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'user', 'booking')
    list_filter = ('rating', 'user', 'booking')
    search_fields = ('rating', 'user__username', 'booking__description')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'status')
    list_filter = ('status', 'client', 'date')
    search_fields = ('client__username', 'service__description')


admin.site.register(Rating, RatingAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking, BookingAdmin)
