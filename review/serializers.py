from rest_framework import serializers
from .models import Review


class ReviewEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('ComplaintId', 'UserId', 'Response', 'Comment', 'Created')


class ReviewAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('ComplaintId', 'UserId', 'Response', 'Comment')
