from grappelli.templatetags.grp_tags import User
from .serializers import ServiceSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from service.models import Service
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdmin, IsClient, IsUsta





class OnlyAdmin(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (IsAdmin, )
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class OnlyAdminPk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin ,GenericAPIView):
    permission_classes = (IsAdmin,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OnlyUser(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class OnlyUserPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class OnlyUsta(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (IsUsta, )
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OnlyUstaPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsUsta, )
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)





    



    
    
