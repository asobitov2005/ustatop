from django.urls import path, include


urlpatterns = [
    path('service/', include('api.service.urls')),
    path('booking/', include('api.booking.urls')),
]
