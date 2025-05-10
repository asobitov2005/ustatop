# from django.urls import path 
# from .views import BookingMixinAPIViewPk, BookingMixinAPIView

# urlpatterns = [
#     path('', BookingMixinAPIView.as_view(), name='booking'),
#     path('<int:pk>/', BookingMixinAPIViewPk.as_view(), name='booking-pk'),
# ]


from rest_framework.routers import DefaultRouter
from .views import  BookingViewSet  

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='bookings')  

urlpatterns = router.urls