from django.urls import path 
from .views import OnlyAdminPk, OnlyUser, OnlyAdmin, OnlyUsta, OnlyUserPk, OnlyUstaPk

urlpatterns = [
    path('admins/', OnlyAdmin.as_view(), name='admin'),
    path('admins/<int:pk>/', OnlyAdminPk.as_view(), name='adminPk'),

    path('clients/', OnlyUser.as_view(), name='user'),
    path('clients/<int:pk>/', OnlyUserPk.as_view(), name='userPk'),

    path('usta/', OnlyUsta.as_view(), name='userPk'),
    path('usta/<int:pk>/', OnlyUstaPk.as_view(), name='userPk'),
]
