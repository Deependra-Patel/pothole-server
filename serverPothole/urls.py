from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
import complaint.urls

urlpatterns = [
    url(r'^complaint/', include(complaint.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]