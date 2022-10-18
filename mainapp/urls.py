from django.urls import path, include
from .import views
from rest_framework import routers
from .views import*

urlpatterns = [
    # path('community/', CommunityViewDashboard.as_view({"get": "list", "post": "create", "delete": "destroy"}), name='basic_view'),
    # path('community/update/<int:pk>/', UpdateCommunityViewDashboard.as_view(), name='basic_view'),
    # path('country/', CountryView.as_view({"get": "list", "post": "create", "delete": "destroy"}), name='basic_view'),
    # path('country/update/<int:pk>/', UpdateCountryView.as_view(), name='basic_view'),
    # path('Job/', JobView.as_view({"get": "list", "post": "create", "delete": "destroy","update": "update"}), name='basic_view'),
    # path('Job/update/<int:pk>/', UpdateJobView.as_view(), name='basic_view'),
    # path('jobapplication/', JobApplicationView.as_view({"get": "list", "post": "create", "delete": "destroy"}), name='basic_view'),
    # path('jobapplication/<int:pk>/', UpdateJobApplicationView.as_view(), name='basic_view'),
    path('jobcatagaries/', jobCatagariesView.as_view({"get": "list", "post":"create"}), name='basic_view'),
    path('catagaries_form/', catagaries_formView.as_view({"get": "list", "post":"create"}), name='basic_view'),
    
    

     
]