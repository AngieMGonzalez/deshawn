
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):

    def retrieve(self, request, pk=None):
        # To serialize a single city (1 row)
        # Step 1: Get a single city based on the primary key in the request URL
        city = City.objects.get(pk=pk)
        # Step 2: Serialize the city record as JSON
        serialized = CitySerializer(city, context={'request': request})

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        # To serialize a list of cities (multiple rows)
        # Step 1: Get all city data from the database
        cities = City.objects.all()
        # Step 2: Convert the data to JSON format
        serialized = CitySerializer(cities, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)


class CitySerializer(serializers.ModelSerializer):
    # Serializing a City Instance
    # It has a sub-class named Meta
    # You specify which database model you want to use
    # You specify which fields in the model should be serialized
    class Meta:
        model = City
        fields = ('id', 'name',)
