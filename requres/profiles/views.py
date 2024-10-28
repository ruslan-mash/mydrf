# Create your views here.

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

from . import serializers, models


class UserView(viewsets.ModelViewSet):
    queryset = models.UserSupport.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.FullDataSerializer


# class RetrieveView(viewsets.ModelViewSet):
#     queryset = models.UserSupport.objects
#     permission_classes = [AllowAny]
#     serializer_class = serializers.UserViewRetriveSerializer




