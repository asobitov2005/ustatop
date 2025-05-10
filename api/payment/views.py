from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import PaymentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsUsta, IsAdmin, IsClient
from django_filters.rest_framework import DjangoFilterBackend
from payment.models import Payment


class OnlyUser(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OnlyUserPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OnlyUsta(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(service__usta=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OnlyUstaPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(service__usta=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OnlyAdmin(viewsets.ModelViewSet):
    permission_classes = (IsAdmin,)
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend]
