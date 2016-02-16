from django.shortcuts import render

from .models import User
from django.http import Http404

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetUsers(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserEntrySerializer(users, many=True)
		return Response(serializer.data)


class AddUser(APIView):
	def post(self, request, format=None):
		serializer = UserEntrySerializer(data = request.data)       
		if serializer.is_valid():
			serializer.save()  
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
