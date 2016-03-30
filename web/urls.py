"""
URL Mapping for Web version of the app
All web related links have to be served from here
"""
from django.conf.urls import url
from .views import AllComplaints

urlpatterns = [
    url(r'^allComplaints', AllComplaints.as_view(), name='all_complaints')
]
