from rest_framework import status as status_codes
import sys
from django.contrib.auth.models import User


class CreateUserService():


    def create_user(self, data) -> dict:
        user=User.objects.create_user(data['username'], password=data['password'])
        if 'is_superuser' not in data:
            user.is_superuser=False
        else:
            user.is_superuser=data['is_superuser']
        
        if 'is_staff' not in data:
            user.is_staff=False
        else:
            user.is_staff=data['is_staff']
            
        user.save()



      
        response = {
            'success': True,
            'user_id ': user.id
        }

        return response