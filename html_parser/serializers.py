from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    """Url base serializer"""
    url = serializers.URLField()

    class Meta:
        model = Url
        fields = ['id', 'url']
