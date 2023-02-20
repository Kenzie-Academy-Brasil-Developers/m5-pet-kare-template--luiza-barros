from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from .models import SexChoices


class PetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexChoices.choices, default=SexChoices.DEFAULT
    )
    id = serializers.IntegerField(read_only=True)

    group = GroupSerializer()
    traits = TraitSerializer(many=True)
