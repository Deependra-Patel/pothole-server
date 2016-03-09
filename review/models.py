from __future__ import unicode_literals

from django.db import models
from complaint.models import Complaint
from user.models import User


class Review(models.Model):
    ComplaintId = models.ForeignKey(Complaint)
    UserId = models.ForeignKey(User)
    Response = models.CharField(max_length=1) #y-yes it is a pothole, n-not pothole, m-maybe
    Comment = models.CharField(max_length=100, null=True, blank=True)
    Created = models.DateTimeField(auto_now_add=True)
# Create your models here.
