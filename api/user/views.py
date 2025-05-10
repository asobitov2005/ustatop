from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from user.models import CustomUser
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsUsta, IsAdmin, IsClient


class Generic(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        if request.user.is_role == 'superuser':
            return Response({"massage": f"Salom super user{request.user.username}"})
        elif request.user.is_role == "usta":
            return Response({"massage": f"Salom usta{request.user.username}"})
        else:
            return Response({"massage": f"Salom client {request.user.username}"})

class OnlyAdmin(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = [IsAdmin]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OnlyAdminPk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    permission_classes = (IsAdmin,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OnlyUsta(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OnlyUstaPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)





class OnlyUser(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OnlyUserPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


