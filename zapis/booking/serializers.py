
from rest_framework import serializers

from authentication.models import User
from booking.models import Schedule, Services


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'name', 'price')
        depth = 1


class SchedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'user', 'service', 'sched_date', 'sched_time')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff')
        depth = 1

    # def create(self, validated_data):
    #     # Ничего не делаем здесь, чтобы сериализатор не создавал новых пользователей
    #     pass
