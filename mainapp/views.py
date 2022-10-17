
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
    queryset = community.objects.all()
    serializer_class = CommunitySerializer
    parser_classes = (FormParser, MultiPartParser)


class UpdateCommunityViewDashboard(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CommunitySerializer
    parser_classes = (FormParser, MultiPartParser)

    

    def get_object(self):
        try:
            return community.objects.get(id=self.kwargs.get('pk'))
        except community.DoesNotExist:
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

class CountryView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # parser_classes = (FormParser, MultiPartParser)


class UpdateCountryView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CountrySerializer
    # parser_classes = (FormParser, MultiPartParser)

    

    def get_object(self):
        try:
            return Job.objects.get(id=self.kwargs.get('pk'))
        except Job.DoesNotExist:
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

class JobView(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    parser_classes = (FormParser, MultiPartParser)


class UpdateJobView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = JobSerializer
    parser_classes = (FormParser, MultiPartParser)

    

    def get_object(self):
        try:
            return Job.objects.get(id=self.kwargs.get('pk'))
        except Job.DoesNotExist:
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




class JobApplicationView(ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    parser_classes = (FormParser, MultiPartParser)


class UpdateJobApplicationView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = JobApplicationSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        data = request.data
        print(data)



class jobCatagariesView(ModelViewSet):
    queryset = jobCatagaries.objects.all()
    serializer_class = jobCatagaries
    parser_classes = (FormParser, MultiPartParser)



class catagaries_formView(ModelViewSet):
    queryset = catagaries_form.objects.all()
    serializer_class = catagaries_formSerializer
    parser_classes = (FormParser, MultiPartParser)