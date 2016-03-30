"""
This file basically contains views for the web page rendering
"""
from django.shortcuts import render
from rest_framework.views import APIView


class AllComplaints(APIView):
    """
    renders a map which displays all the reports of potholes/speed-breakers on it
    """

    def get(self, request):
        """
        simple get request
        """
        return render(request, 'web/complaints.html')
