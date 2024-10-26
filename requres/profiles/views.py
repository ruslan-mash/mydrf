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

    # serializer_classes = {"retrieve": serializers.UserViewRetrieveSerializer}

    @action(detail=True, methods=['GET'])
    def retrieve_by_id(self, request, pk=None):
        queryset = models.UserProfile.objects.get(pk=pk)
        serializer = serializers.UserSerializer(queryset)
        return Response(serializer.data)

    # def get_queryset(self):
    #     if self.action == "retrieve":
    #         self.get_serializer()
    #
    #         serializer = serializers.UserViewRetrieveSerializer(pk=self.kwargs.get("pk"))
    #     return self.queryset.filter(id=self.kwargs.get("pk"))
