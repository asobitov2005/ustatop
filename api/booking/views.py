from .serializers import BookingSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from service.models import Booking
from rest_framework import viewsets
from api.permissions import IsUsta, IsAdmin, IsClient
from django_filters.rest_framework import DjangoFilterBackend




class OnlyUser(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OnlyUserPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OnlyUsta(mixins.ListModelMixin, mixins.CreateModelMixin ,GenericAPIView):
    permission_classes = (IsClient,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OnlyUstaPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin,]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]