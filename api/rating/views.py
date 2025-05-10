from grappelli.templatetags.grp_tags import User

from .serializers import RatingSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from service.models import Rating
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RatingSerializer
from .filters import RatingFilter
from api.permissions import IsClient, IsAdmin, IsUsta
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins




class OnlyUser(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OnlyUserPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsClient,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OnlyUsta(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OnlyUstaPk(mixins.RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsUsta,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)





class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin,]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter
