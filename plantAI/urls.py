"""plantAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import CustomObtainAuthToken
from main.views import UserCreate, PlantsView
from diseases.views import DiseaseDetectionView, DiseaseImageUploadToImagekitView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('create-user/', UserCreate.as_view(), name='account-create'),
    path('plants-view/', PlantsView.as_view(), name='plants-view'),
    path('detect-disease/', DiseaseDetectionView.as_view(), name='detect-disease'),
    path('upload-imagekit/', DiseaseImageUploadToImagekitView.as_view(), name='upload-imagekit')
]
