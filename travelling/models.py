from django.db import models


class Locations(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(upload_to="pic")
  price = models.IntegerField()
  status = models.TextField()
  offer = models.BooleanField(default=False)
  