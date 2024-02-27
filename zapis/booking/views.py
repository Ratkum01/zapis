from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from authentication.models import User
from authentication.serializers import UserSerializer
from booking.models import Services, Schedule
from booking.serializers import ServiceSerializer, SchedSerializer


class ServiceApiView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SchedApiView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = SchedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', ]
