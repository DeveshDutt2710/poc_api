from django.urls import path
from .create_user_views import (CreateUser)

urlpatterns = [
    path('create/', CreateUser.as_view(), name="create_user_and_password"),
]
