from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

import sys
import os
import pandas as pd
from pymongo import MongoClient  


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  
  def post(self, request, *args, **kwargs):
    excel_file = request.data['file']

    read_file = pd.read_excel(excel_file)
    read_file.to_csv("Test.csv", index = None,header=True)

    os.system("mongoimport --host=127.0.0.1:27017 -d excel_to_mongodb -c excel_mongodb --type csv --file Test.csv --headerline")
    os.remove('Test.csv')

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)