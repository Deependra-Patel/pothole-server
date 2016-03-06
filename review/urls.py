from django.conf.urls import url, include
from .views import ReviewList, ReviewDetail

urlpatterns = [
    url(r'^$', ReviewList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', ReviewDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]