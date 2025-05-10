from .serializers import BookingSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from service.models import Booking
from .filters import BookingFilter
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated




# class BookingMixinAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)   


# class BookingMixinAPIViewPk(mixins.ListModelMixin, mixins.CreateModelMixin,  mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookingFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user)