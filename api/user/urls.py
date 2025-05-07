from django.urls import path, include
from .views import UserAPIViewMixin, UserDetailAPIViewMixin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', UserAPIViewMixin.as_view()),
    path('<int:pk>/', UserDetailAPIViewMixin.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]