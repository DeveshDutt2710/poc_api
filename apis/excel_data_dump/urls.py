from django.urls import path
from .excel_data_dump_views import (FileView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('upload_file/', FileView.as_view(), name="upload_file"),
    
]
