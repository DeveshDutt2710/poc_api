from django.urls import path, include

urlpatterns=[
    path('nearest_city/', include('apis.nearest_city.urls')),
    path('create_user/', include('apis.create_user.urls')),
    path('excel_data_dump/', include('apis.excel_data_dump.urls')),
]