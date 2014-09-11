
from django.db import models
# Create your models here.

class novice(models.Model):

    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='static/img')

