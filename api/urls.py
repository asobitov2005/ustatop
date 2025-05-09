from django.urls import path, include


urlpatterns = [
    path('service/', include('api.service.urls')),
    path('booking/', include('api.booking.urls')),
    path('rating/', include('api.rating.urls')),
    path('user/', include('api.user.urls')),
    path('address/', include('api.address.urls')),
    path('city/', include('api.city.urls'))
]
