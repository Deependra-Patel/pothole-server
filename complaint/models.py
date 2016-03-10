from __future__ import unicode_literals

from django.db import models
from user.models import User

from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from serverPothole import settings


class Complaint(models.Model):
    ReporterId = models.ForeignKey(User, on_delete = models.CASCADE)
    Location = models.PointField(srid=4326)
    City = models.CharField(max_length=3)
    Fixed = models.BooleanField(default='False')
    #'p' - pothole, 's'- speedbreaker
    Type = models.CharField(max_length=1, default='p')
    #'a'-Added, 'r'-reviewed, 'd'-resolved, 'f'-falseReport
    Status = models.CharField(max_length=1, default='a')
    Severity = models.IntegerField(default=5, blank=True)
    Image = models.ImageField("Image", upload_to=settings.MEDIA_ROOT+"/images")
    Info = models.CharField(max_length=300, null=True, blank=True)
    Created = models.DateTimeField(auto_now_add=True)

    def latitude(self):
        return self.Location.y

    def longitude(self):
        return self.Location.x

    def __str__(self):
        return "Id "+str(self.id)+", ReporterId "+str(self.ReporterId)+" "+self.Status

