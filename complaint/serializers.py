from rest_framework import serializers
from .models import Complaint


class ComplaintEntrySerializer(serializers.ModelSerializer):
    Lat = serializers.CharField(source='latitude')
    Long = serializers.CharField(source='longitude')

    class Meta:
        model = Complaint
        fields = ('id', 'ReporterId', 'City', 'Fixed', 'Type', 'Status', 'Severity', 'Image', 'Info', 'Created',
                  'Lat', 'Long')


class ComplaintAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('ReporterId', 'City', 'Type', 'Severity', 'Image', 'Info')
