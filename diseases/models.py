from django.db import models
from main.models import Plants


class Uploads(models.Model):
    photo = models.ImageField(upload_to='uploads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Diseases(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=50)
    plant_id = models.ForeignKey(Plants, on_delete=models.CASCADE)

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
