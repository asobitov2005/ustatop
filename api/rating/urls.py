from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, OnlyUser, OnlyUserPk, OnlyUsta, OnlyUstaPk

router = DefaultRouter()
router.register(r'ratings', AdminViewSet)

urlpatterns = [
    path('client/', OnlyUser.as_view()),
    path('client/<int:pk>', OnlyUserPk.as_view()),

    path('usta/', OnlyUsta.as_view()),
    path('usta/<int:pk>', OnlyUstaPk.as_view()),


    path('admins/', include(router.urls)),
]
