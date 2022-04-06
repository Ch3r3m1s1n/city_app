from rest_framework import serializers
from .models import City, Citizen


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = (
            'firstname',
            'lastname',
            'middlename',
        )


class CitySerializer(serializers.ModelSerializer):
    citizens = CitizenSerializer(many=True)

    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'citizens',
        )
