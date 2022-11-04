
from crypt import methods
import imp
from unicodedata import name
from django.shortcuts import render
from .models import *
from .serializer import *
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .save_mangodb import save_catagaries_form
import requests
# Create your views here.
class research_JobView(ModelViewSet):
    queryset = research_Job.objects.all()
    serializer_class = research_JobSerializer
    parser_classes = (FormParser, MultiPartParser)


class Update_research_JobView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = research_JobSerializer
    parser_classes = (FormParser, MultiPartParser)

    

    def get_object(self):
        try:
            return research_Job.objects.get(id=self.kwargs.get('pk'))
        except research_Job.DoesNotExist:
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




# class JobApplicationView(ModelViewSet):
#     queryset = JobApplication.objects.all()
#     serializer_class = research_ApplicationSerializer
#     parser_classes = (FormParser, MultiPartParser)


# class UpdateJobApplicationView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = research_ApplicationSerializer
#     parser_classes = (FormParser, MultiPartParser)

#     def post(self, request):
#         data = request.data
#         print(data)




@method_decorator(csrf_exempt, name='dispatch')
class catagaries_formView(APIView):
    serializer_class = catagaries_formSerializer
    parser_classes = (FormParser, MultiPartParser)

    def get(self, request):
        snippets = catagaries_form.objects.all()
        serializer = self.serializer_class(snippets, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            try:
                save_catagaries_form(serializer.data)
            except:
                print("Candidate data not saved to MongoDB Database")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

