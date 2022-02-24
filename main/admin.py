from django.contrib import admin
from .models import Plants
from diseases.models import Diseases, Uploads, Cure, DetectionHistory
# Register your models here.

admin.site.register(Plants)
admin.site.register(Diseases)
admin.site.register(Cure)
admin.site.register(DetectionHistory)
