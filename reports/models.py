from django.db import models

from diseases.models import DetectionHistory


class Reports(models.Model):
    history = models.ForeignKey(DetectionHistory, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Report"
