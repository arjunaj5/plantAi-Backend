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
from diseases.views import DiseaseDetectionView, DiseaseImageUploadToImagekitView, UserHistory, DetailsFromDiseaseId
from reports.views import ReportsCreationView, ReportsRetrievalView, AllReportsRetrievalView, NewDiseaseView, NewCureView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('create-user/', UserCreate.as_view(), name='account-create'),
    path('plants-view/', PlantsView.as_view(), name='plants-view'),
    path('detect-disease/', DiseaseDetectionView.as_view(), name='detect-disease'),
    path('upload-imagekit/', DiseaseImageUploadToImagekitView.as_view(), name='upload-imagekit'),
    path('user-history/', UserHistory.as_view(), name='user-history'),
    path('detection-details-by-disease-id/', DetailsFromDiseaseId.as_view(), name='details-from-disease-id'),
    path('disease-reports-creation/', ReportsCreationView.as_view(), name='reports-creation-view'),
    path('reports-retrieval-view/', ReportsRetrievalView.as_view(), name='reports-retrieval-view'),
    path('all-reports-retrieval-view/', AllReportsRetrievalView.as_view(), name='all-reports-retrieval-view'),

    path('new-disease-health-dept/', NewDiseaseView.as_view(), name='new-disease-health-dept'),
    path('new-cure-health-dept/', NewCureView.as_view(), name='new-cure-health-dept')
]
