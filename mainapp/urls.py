from django.urls import path, include
from .import views
from rest_framework import routers
from .views import*

urlpatterns = [
    path('research_job/', research_JobView.as_view({"get": "list", "post": "create", "delete": "destroy","update": "update"}), name='basic_view'),
    path('research_job/update/<int:pk>/', Update_research_JobView.as_view(), name='basic_view'),
    # path('jobapplication/', JobApplicationView.as_view({"get": "list", "post": "create", "delete": "destroy"}), name='basic_view'),
    # path('jobapplication/<int:pk>/', UpdateJobApplicationView.as_view(), name='basic_view'),
    path('catagaries_form/', catagaries_formView.as_view(), name='basic_view'),
    
    

     
]