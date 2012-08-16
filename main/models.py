from django.db import models

# Create your models here.

class Anime(models.Model):
    title = models.CharField(60)
    demography = models.CharField(30)
    