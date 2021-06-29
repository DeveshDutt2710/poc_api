from django.urls import path
from .nearest_city_views import (GetNearestCityView)

urlpatterns = [
    path('fetch/', GetNearestCityView.as_view(), name="fetch_nearest_city_by_distance"),
    
]
