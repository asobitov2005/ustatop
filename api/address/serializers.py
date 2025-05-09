from rest_framework import serializers
from user.models import CustomUser

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'