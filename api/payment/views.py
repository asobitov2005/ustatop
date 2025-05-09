from rest_framework.response import Response
from rest_framework import status
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view, permission_classes
from payment.models import Payment
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



class PaymentAPIViewMixin(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated, ]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PaymentDetailAPIViewMixin(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated, ]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)