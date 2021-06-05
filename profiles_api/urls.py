from django.contrib.auth import base_user
from django.urls import path, include
from rest_framework import routers, viewsets
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet, base_name='profile')
router.register('feed',views.UserProfileFeedViewSet, base_name='feed')

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view(),name='hello-view'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('',include(router.urls)),
]