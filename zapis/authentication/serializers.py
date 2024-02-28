from rest_framework import serializers
from authentication.models import User
from authentication.task import  mock_otp_verification
class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}
