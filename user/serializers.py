from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

_user_fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = _user_fields


class UserTokenSerializer(serializers.BaseSerializer):
    user_fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'token')

    def to_internal_value(self, data):
        values = {}
        
        for field in self.user_fields:
            values[field] = getattr(data, field)
        
        return values
    
    def to_representation(self, obj):
        data = {}

        for field in self.user_fields:
            data[field] = getattr(obj, field)
        
        return data