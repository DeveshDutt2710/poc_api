from django.urls import path
from .nearest_city_views import (GetNearestCityView, HelloView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('fetch/', GetNearestCityView.as_view(), name="fetch_nearest_city_by_distance"),
    path('hello/', HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
