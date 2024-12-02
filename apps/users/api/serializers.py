from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'password', 'company', 'customer', 'is_staff', 'is_active', 'is_verified']
