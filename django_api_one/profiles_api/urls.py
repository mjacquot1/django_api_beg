from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello'),
    path('goodbye-view/', views.GoodbyeApiView.as_view(), name='goodbye'),
    path('', include(router.urls))
]