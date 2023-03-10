from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializers import PetSerializer
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from .models import Pet
from traits.models import Trait
from groups.models import Group
from rest_framework.pagination import PageNumberPagination


class PetView(APIView, PageNumberPagination):
    def get(self, request):
        trait = request.query_params.get("trait", None)

        if trait:
            pets = Pet.objects.filter(traits__name=trait).all()
        else:
            pets = Pet.objects.all()

        result_page = self.paginate_queryset(pets, request)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group_dict = serializer.validated_data.pop("group")
        traits_list = serializer.validated_data.pop("traits")

        pet_obj = Pet.objects.create(**serializer.validated_data)

        for trait_dict in traits_list:
            trait_obj = Trait.objects.filter(
                name__iexact=trait_dict["name"].lower()
            ).first()

            if not trait_obj:
                trait_obj = Trait.objects.create(**trait_dict)

            pet_obj.traits.add(trait_obj)

        group_obj = Group.objects.filter(
            scientific_name__iexact=group_dict["scientific_name"].lower()
        ).first()

        if not group_obj:
            group_obj = Group.objects.create(**group_dict)

        pet_obj.group = group_obj

        serializer = PetSerializer(pet_obj)
        return Response(serializer.data, status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, request, pet_id):
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        serializer = PetSerializer(pet)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pet_id):
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
