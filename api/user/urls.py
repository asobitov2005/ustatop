from django.urls import path, include
from .views import OnlyUser, OnlyAdmin, OnlyAdminPk, OnlyUsta, OnlyUserPk, OnlyUstaPk
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admins/', OnlyAdmin.as_view()),
    path('adminPk/<int:pk>/', OnlyAdminPk.as_view()),

    path('clients/', OnlyUser.as_view()),
    path('clientPk/<int:pk>/', OnlyUserPk.as_view()),

    path('usta/', OnlyUsta.as_view()),
    path('ustaPk/<int:pk>/', OnlyUserPk.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]