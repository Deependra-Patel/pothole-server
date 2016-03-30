"""serverPothole URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^api/complaint/', include('complaint.urls', namespace='complaint')),
    url(r'^api/user/', include('user.urls', namespace='user')),
    url(r'^api/review/', include('review.urls', namespace='review')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'),
        name='api-auth'),
    url(r'^web/', include('web.urls', namespace='web'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
