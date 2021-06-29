from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from .nearest_city_service import NearestCityService




class GetNearestCityView(APIView):

    def get(self, request, *args, **kwargs):

        nearest_city_manager = NearestCityService()
        response = nearest_city_manager.get_nearest_city_by_distance(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)

