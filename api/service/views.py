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
    


    # class DetailCategoryView(APIView):
    
    # def get_object(self,pk):
    #     category = get_object_or_404(Category, pk=pk)
    #     return category


    # def get(self,request, pk ):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category, request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        
    # def delete(self, request, pk):
    #     category = self.get_object(pk)
    #     category.delete()
    #     return Response({'data':'deleted'})
    
    
