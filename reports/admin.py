from django.contrib import admin

from .models import Reports, NewCure, NewDisease

admin.site.register(Reports)
admin.site.register(NewDisease)
admin.site.register(NewCure)
