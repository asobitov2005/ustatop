from rest_framework import serializers 
from service.models import  Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
