from django.urls import path
from .views import get_user, verify_user

urlpatterns = [
    path('get/', get_user),
    path('check/', verify_user)
]