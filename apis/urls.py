from django.urls import path, include

urlpatterns=[
    path('nearest_city/', include('apis.nearest_city.urls')),
]