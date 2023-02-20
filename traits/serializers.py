from rest_framework import serializers


class TraitSerializer(serializers.Serializer):
    trait_name = serializers.CharField(source="name", max_length=20)
    created_at = serializers.DateField(read_only=True)
    id = serializers.IntegerField(read_only=True)
