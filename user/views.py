"""
user app views
"""
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from complaint.models import Complaint
from complaint.serializers import ComplaintEntrySerializer
from user.models import User
from .serializers import UserEntrySerializer


class UserList(APIView):
    """
    Add user or get all users
    """

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserEntrySerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserEntrySerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserEntrySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFromEmail(APIView):
    """
    Gives user details given Email(Only not deActivated users)
    """

    def post(self, request, format=None):
        try:
            user = User.objects.get(Email=request.data["Email"], DeActivate=False)
            serializer = UserEntrySerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise Http404


class UserGetComplaintForReview(APIView):
    """
    Gives list of complaints (at most 3) nearby to user for review
    """

    def get(self, request, pk, format=None):
        complaints = Complaint.objects.filter(Status='a').exclude(ReporterId=pk).exclude(
            review__UserId=pk)[:3]
        complaints = ComplaintEntrySerializer(complaints, many=True)
        return Response(complaints.data)
