from rest_framework import serializers

from authentication.models import People
from authentication.serializers import PeopleSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        people_data = validated_data.pop('people')
        people = People.objects.create_people(**people_data)
        user = User.objects.create(people=people, **validated_data)
        return user