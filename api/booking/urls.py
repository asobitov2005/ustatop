from django.urls import path 
from .views import BookingMixinAPIViewPk, BookingMixinAPIView

urlpatterns = [
    path('', BookingMixinAPIView.as_view(), name='booking'),
    path('<int:pk>/', BookingMixinAPIViewPk.as_view(), name='booking-pk'),
]
