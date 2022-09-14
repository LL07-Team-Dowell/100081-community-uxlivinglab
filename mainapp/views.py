
from django.shortcuts import render
from .models import *
from .serializer import *
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
import requests
# Create your views here.

class CommunityViewDashboard(ModelViewSet):
    queryset = CommunityTable.objects.all()
    serializer_class = CommunitySerlizer
    parser_classes = (FormParser, MultiPartParser)


class UpdateCommunityViewDashboard(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CommunitySerlizer
    parser_classes = (FormParser, MultiPartParser)

    

    def get_object(self):
        try:
            return CommunityTable.objects.get(id=self.kwargs.get('pk'))
        except CommunityTable.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object()
        serializer = self.serializer_class(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

