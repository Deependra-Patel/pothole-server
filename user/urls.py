from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .views import GetUsers, AddUser

urlpatterns = [
    url(r'^GetUsers', GetUsers.as_view()),
    url(r'^AddUser', AddUser.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]