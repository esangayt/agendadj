from rest_framework import serializers


class LoginSocialSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
