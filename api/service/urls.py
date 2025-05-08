from django.urls import path 
from .views import ServiceMixinAPIViewPk, ServiceMixinAPIView

urlpatterns = [
    path('', ServiceMixinAPIView.as_view(), name='service'),
    path('<int:pk>/', ServiceMixinAPIViewPk.as_view(), name='service-pk'),
]
