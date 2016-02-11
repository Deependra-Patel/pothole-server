from django.conf.urls import url, include
from django.contrib.auth.models import User
import complaint.urls

urlpatterns = [
    url(r'^complaint/', include(complaint.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]