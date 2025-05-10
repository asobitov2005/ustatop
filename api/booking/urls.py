from django.urls import path, include
from .views import OnlyUsta, OnlyUstaPk, OnlyUser, OnlyUserPk, AdminViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', AdminViewSet)

urlpatterns = [
    path('client/', OnlyUser.as_view(), name='clien'),
    path('client/<int:pk>/', OnlyUserPk.as_view(), name='clienPk'),

    path('usta/', OnlyUsta.as_view(), name='usta'),
    path('usta/<int:pk>', OnlyUstaPk.as_view(), name='ustaPk'),

    path('admins/', include(router.urls), name='admin'),
]