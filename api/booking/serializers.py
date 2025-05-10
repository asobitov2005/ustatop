from rest_framework import serializers 
from service.models import Booking, CustomUser, Service
from datetime import date


class BookingSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'client', 'service', 'status', 'date']
        read_only_fields = ['id']

    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return value
    
    def validate_status(self, value):
        if self.instance and self.instance.status == 'yakunlangan' and value != 'yakunlangan':
            raise serializers.ValidationError("Cannot change status after 'yakunlangan'.")
        return value