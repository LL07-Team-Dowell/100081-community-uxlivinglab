from django.urls import path, include
from .import views
from rest_framework import routers
from .views import*
router = routers.DefaultRouter()

router.register("Community-operations", views.CommunityViewDashboard)
urlpatterns = [
  
  
     path("", include(router.urls)),
       
     
]