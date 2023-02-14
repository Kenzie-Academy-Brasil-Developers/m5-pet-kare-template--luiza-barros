from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    scientific_name = serializers.CharField(source="name", max_length=50, unique=True)
    created_at = serializers.DateTimeField(read_only=True, auto_now_add=True)
    id = serializers.IntegerField(read_only=True)
