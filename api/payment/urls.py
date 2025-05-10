from django.urls import path, include
from .views import OnlyUsta, OnlyUstaPk, OnlyUser, OnlyUserPk, OnlyAdmin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', OnlyAdmin)

urlpatterns = [
    path('client/', OnlyUser.as_view()),
    path('client/<int:pk>/', OnlyUserPk.as_view()),

    path('usta/', OnlyUsta.as_view()),
    path('usta/<int:pk>/', OnlyUstaPk.as_view()),

    path('admins/', include(router.urls)),

]