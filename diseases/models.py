from django.db import models
from main.models import Plants
from django.contrib.auth.models import User


class Uploads(models.Model):
    photo = models.ImageField(upload_to='uploads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Uploads"


class Diseases(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=50)
    ml_id = models.IntegerField(unique=True)
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disease"


class Cure(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    diseases = models.ManyToManyField(Diseases)

    def __str__(self):
        return self.name


class DetectionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, default=None, blank=True, null=True, on_delete=models.CASCADE)
    detected = models.BooleanField(default=True)
    leaf_url = models.CharField(max_length=255)

    def __str__(self):
        return self.detected
