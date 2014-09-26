
from django.db import models
# Create your models here.


class exercises(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    shown_on_main_page = models.BooleanField()


class picture_gallery(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class novice(models.Model):

    title = models.TextField()
    content = models.TextField()





