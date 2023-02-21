from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    scientific_name = serializers.CharField(source="name")
    created_at = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
