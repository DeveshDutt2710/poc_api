from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from rest_framework.response import Response
from .nearest_city_service import NearestCityService
from rest_framework.permissions import IsAuthenticated



class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class GetNearestCityView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request, *args, **kwargs):

        nearest_city_manager = NearestCityService()
        response = nearest_city_manager.get_nearest_city_by_distance(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)

