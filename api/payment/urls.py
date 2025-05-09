from django.urls import path, include
from .views import PaymentAPIViewMixin, PaymentDetailAPIViewMixin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', PaymentAPIViewMixin.as_view()),
    path('<int:pk>/', PaymentDetailAPIViewMixin.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]