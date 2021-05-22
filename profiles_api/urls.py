from django.urls import path, include
from rest_framework import routers, viewsets
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view(),name='hello-view'),
    path('',include(router.urls)),
]