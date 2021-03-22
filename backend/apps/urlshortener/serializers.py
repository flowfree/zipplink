from rest_framework import serializers
from apps.urlshortener.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('id', 'long_url', 'short_url', 'created_at')

    def create(self, validated_data):
        long_url = validated_data['long_url']
        obj, _ = URL.objects.get_or_create(long_url=long_url)
        return obj
