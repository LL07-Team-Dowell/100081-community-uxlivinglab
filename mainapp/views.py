from genericpath import commonprefix
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CommunityViewDashboard(ModelViewSet):
    queryset = CommunityTable.objects.all()
    serializer_class = CommunitySerlizer
 