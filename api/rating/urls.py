from django.urls import path, include
from .views import RatingMixinAPIViewPk, RatingMixinAPIView, RatingSerializer
from rest_framework.routers import DefaultRouter
from .views import RatingViewSet

router = DefaultRouter()
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    # path('', RatingMixinAPIView.as_view(), name='rating'),
    path('<int:pk>/', RatingMixinAPIViewPk.as_view(), name='rating-pk'),
    path('', include(router.urls)),
]
