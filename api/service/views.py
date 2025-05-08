from .serializers import ServiceSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from service.models import Service



class ServiceMixinAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   


class ServiceMixinAPIViewPk(mixins.ListModelMixin, mixins.CreateModelMixin,  mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)