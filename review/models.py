from django.db import models
from complaint.models import Complaint
from user.models import User
from core.utils import REVIEW_RESPONSE_TYPE


class Review(models.Model):
    """
    All reviews of complaints are stored here
    """
    ComplaintId = models.ForeignKey(Complaint)
    UserId = models.ForeignKey(User)
    Response = models.CharField(max_length=1, choices=REVIEW_RESPONSE_TYPE)
    Comment = models.CharField(max_length=100, null=True, blank=True)
    Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        To ensure one user per complaint
        """
        unique_together = ('ComplaintId', 'UserId')
