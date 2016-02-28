from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
import complaint.urls
import user.urls
from django.conf.urls.static import static
import settings

urlpatterns = [
    url(r'^complaint/', include(complaint.urls)),
    url(r'^user/', include(user.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)