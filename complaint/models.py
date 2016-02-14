from __future__ import unicode_literals

from django.db import models
from user.models import User

from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry

class Complaint(models.Model):
	ReporterId = models.ForeignKey(User, on_delete = models.CASCADE)
	# Location = models.PointField(srid=4326)
	City = models.CharField(max_length=3)
	Fixed = models.BooleanField(default='False')
	Reviewed = models.BooleanField(default='False', blank=True)
	#'p' - pothole, 's'- speedbreaker
	Type = models.CharField(max_length=1, default='p')
	Severity = models.IntegerField(default=5, blank=True)
	Image = models.ImageField("Image", upload_to="images/")
	Info = models.CharField(max_length=300, null=True, blank=True)
	Created = models.DateTimeField(auto_now_add=True)

