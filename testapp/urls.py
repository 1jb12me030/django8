from django.db import router
from rest_framework.routers import DefaultRouter
from testapp.views import EmployeeViewSet
from django.urls import path,include


router=DefaultRouter()
router.register('testapp',EmployeeViewSet)

urlpatterns = [
    path('api/',include(router.urls))
]
