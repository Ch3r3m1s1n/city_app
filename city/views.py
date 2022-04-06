from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Citizen, City
from .serializers import CitySerializer


def main(request):
    citizens = Citizen.objects.all()
    top_cities = City.objects.annotate(citizen_count=Count('citizens')).order_by('-citizen_count')[:10]

    return render(request, 'main.html', {'citizens': citizens, "top_cities": top_cities})


def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city_detail.html', {'city': city})


class CityAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        name = self.request.query_params.get("name") or ''
        if pk is not None:
            city = City.objects.filter(pk=pk).first()
            citySerializer = CitySerializer(city)
            return Response({"city": citySerializer.data})
        else:
            cities = City.objects.filter(name__contains=name).all()
            citiesSerializer = CitySerializer(cities, many=True)
            return Response(citiesSerializer.data)
