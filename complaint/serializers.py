from rest_framework import serializers
from .models import Complaint
class ComplaintEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Complaint
		fields = ('id', 'ReporterId', 'City', 'Fixed', 'Reviewed', 'Type',
		 'Severity', 'Image', 'Info', 'Created')

class ComplaintAddSerializer(serializers.ModelSerializer):
	class Meta:
		model = Complaint
		fields = ('ReporterId','City', 'Reviewed', 'Type', 'Severity', 'Image', 'Info')