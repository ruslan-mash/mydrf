from rest_framework import serializers

from . import models


class SupportSerializer(serializers.ModelSerializer):
    url = serializers.URLField(label="url", max_length=200)
    text = serializers.CharField(label="text", max_length=500)

    class Meta:
        model = models.UserSupport
        fields = ("url", "text")


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label="идентификатор", source="user_id")
    email = serializers.EmailField(label="электронная почта", max_length=200)
    first_name = serializers.CharField(label="first_name", max_length=500)
    last_name = serializers.CharField(label="last_name", max_length=500)
    avatar = serializers.URLField(label="avatar", max_length=200)

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "first_name", "last_name", "avatar",)


class FullDataSerializer(serializers.Serializer):
    data = UserSerializer(many=True)
    support = SupportSerializer()

    def create(self, validated_data):
        profile_data = validated_data.get("data")
        support_data = validated_data.get("support")
        support = models.UserSupport.objects.create(**support_data)

        for i in profile_data:
            result = models.UserProfile.objects.create(**i)
            support.user_profile.add(result)
        return support

    def to_representation(self, instance):
        serializer = []

        for i in instance.user_profile.all():
            serializer.append(UserSerializer(i).data)
        return {"profile_data": serializer,
                "support": {"url": instance.url,
                            "text": instance.text
                            }
                }

# class UserViewRetriveSerializer(serializers.ModelSerializer):
#     user_profile = UserSerializer(many=True)
#
#     class Meta:
#         model = models.UserSupport
#         fields = ("url", "text", "user_profile",)
