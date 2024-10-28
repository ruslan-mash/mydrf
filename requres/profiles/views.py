# Create your views here.

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

from . import serializers, models


class UserView(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.FullDataSerializer


    # @action(detail=True, methods=['GET']) # вызов http://127.0.0.1:8000/api/users/{pk}/retrieve_by_id
    # def retrieve_by_id(self, request, pk=None):
    #     queryset = models.UserProfile.objects.get(pk=pk)
    #     serializer = serializers.UserSerializer(queryset)
    #     return Response(serializer.data)




