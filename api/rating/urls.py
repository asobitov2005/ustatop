from django.urls import path 
from .views import RatingMixinAPIViewPk, RatingMixinAPIView

urlpatterns = [
    path('', RatingMixinAPIView.as_view(), name='rating'),
    path('<int:pk>/', RatingMixinAPIViewPk.as_view(), name='rating-pk'),
]
