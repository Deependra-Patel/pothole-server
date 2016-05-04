"""
Serializers for user class
"""
from rest_framework import serializers

from .models import User


class UserEntrySerializer(serializers.ModelSerializer):
    """
    Serializer for entry in user table. id, Credit, Rating, DeActivate can be changed only by admin
    or server
    """
    class Meta:
        model = User
        read_only_fields = ('id', 'Credit', 'Rating', 'DeActivate')
        fields = (
            'id', 'Name', 'Address', 'HomeLocation', 'City', 'Phone', 'Email', 'FbId', 'Rating',
            'Credit', 'DeActivate')
