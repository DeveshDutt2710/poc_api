from rest_framework.views import APIView
from rest_framework import status as status_codes
from django.http import JsonResponse
from rest_framework.response import Response
from .create_user_service import CreateUserService




class CreateUser(APIView):

    def get(self, request, *args, **kwargs):

        create_user_manager = CreateUserService()
        response = create_user_manager.create_user(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)

