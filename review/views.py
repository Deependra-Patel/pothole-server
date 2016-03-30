"""
Contains views for all the reviews of complaints by users
"""
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Review
from .serializers import ReviewAddSerializer, ReviewEntrySerializer


class ReviewList(APIView):
    """
    Add Review or get all Reviews
    """

    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewEntrySerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    """
    Retrieve, update or delete a Review instance.
    """

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Review = self.get_object(pk)
        Review = ReviewEntrySerializer(Review)
        return Response(Review.data)

    def put(self, request, pk, format=None):
        Review = self.get_object(pk)
        serializer = ReviewAddSerializer(Review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Review = self.get_object(pk)
        Review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
