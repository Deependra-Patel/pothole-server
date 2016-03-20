from .models import User

from rest_framework import serializers


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'Credit', 'Rating', 'DeActivate')
        fields = ('id', 'Name', 'Address', 'HomeLocation', 'City', 'Phone', 'Email', 'FbId', 'Rating', 'Credit',
                  'DeActivate')