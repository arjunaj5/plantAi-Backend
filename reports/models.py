from django.db import models

from diseases.models import DetectionHistory


class Reports(models.Model):
    history = models.ForeignKey(DetectionHistory, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Report"


class NewDisease(models.Model):
    report = models.ForeignKey(Reports, on_delete=models.CASCADE)
    is_correction = models.BooleanField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    cure_name = models.CharField(max_length=50)
    cure_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "NewDiseases"


class NewCure(models.Model):
    report = models.ForeignKey(Reports, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "NewCure"
