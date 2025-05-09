from django.urls import path, include
from .views import CityAPIViewMixin, CityDetailAPIViewMixin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', CityAPIViewMixin.as_view()),
    path('<int:pk>/', CityDetailAPIViewMixin.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]