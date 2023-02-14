from rest_framework import serializers


class TraitSerializer(serializers.Serializer):
    trait_name = serializers.CharField(source="name", max_length=20, unique=True)
    created_at = serializers.DateField(read_only=True, auto_now_add=True)
    id = serializers.IntegerField(read_only=True)
