from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
