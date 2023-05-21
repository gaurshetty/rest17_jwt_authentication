from django.urls import path, include
from .views import EmployeeCBViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', EmployeeCBViewSet, basename='empviewset')

urlpatterns = [
    path('', include(router.urls)),
]
