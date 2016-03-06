from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.geos import GEOSGeometry

class User(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    HomeLocation = models.PointField(srid=4326, null=True, blank=True)
    City = models.CharField(max_length=3)
    Phone = models.CharField(max_length=10)
    Email = models.CharField(max_length=40, null=True, blank=True)
    FbId = models.CharField(max_length=20, null=True, blank=True)
    Rating = models.FloatField(default=50)
    Credit = models.FloatField(default=0)
    DeActivate = models.BooleanField(default=False)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Id "+str(self.id)+" Name "+self.Name
# Create your models here.
