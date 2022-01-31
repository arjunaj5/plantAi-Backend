from django.db import models

# Create your models here.


class Plants(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Plants"
